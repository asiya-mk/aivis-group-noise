import numpy as np
import pandas as pd
import torch
from transformers import ASTFeatureExtractor, ASTForAudioClassification

from src.label_map import ESC_TO_AUDIOSET, ANIMAL_LABELS

CKPT = "MIT/ast-finetuned-audioset-10-10-0.4593"
SR = 16000
GROUPS = ["animals", "natural", "human", "domestic", "urban"]
# dict order = ESC-50 target order
CLASSES = np.array(list(ESC_TO_AUDIOSET))
GROUP_OF = {c: GROUPS[i // 10] for i, c in enumerate(CLASSES)}


def load_model(device="cpu"):
    fe = ASTFeatureExtractor.from_pretrained(CKPT)
    model = ASTForAudioClassification.from_pretrained(CKPT).to(device).eval()
    labels = np.array([model.config.id2label[i] for i in range(model.config.num_labels)])
    return fe, model, labels


@torch.no_grad()
def predict(fe, model, waves, device="cpu", batch_size=16):
    out = []
    for i in range(0, len(waves), batch_size):
        inputs = fe(waves[i:i + batch_size], sampling_rate=SR, return_tensors="pt").to(device)
        # AudioSet is multi-label, so sigmoid per label, not softmax
        out.append(torch.sigmoid(model(**inputs).logits).cpu().numpy())
    return np.concatenate(out)


def esc_scores(probs, labels):
    idx = {l: i for i, l in enumerate(labels)}
    return np.stack([
        probs[:, [idx[l] for l in ESC_TO_AUDIOSET[c]]].max(1) if ESC_TO_AUDIOSET[c] else np.zeros(len(probs))
        for c in CLASSES
    ], axis=1)


def prediction_table(probs, labels, target=None):
    idx = {l: i for i, l in enumerate(labels)}
    scores = esc_scores(probs, labels)
    order = np.argsort(-scores, axis=1)
    rows = np.arange(len(probs))
    df = pd.DataFrame({
        "pred": CLASSES[order[:, 0]],
        "conf": scores[rows, order[:, 0]],
        "second": CLASSES[order[:, 1]],
        "margin": scores[rows, order[:, 0]] - scores[rows, order[:, 1]],
        "top1_audioset": labels[probs.argmax(1)],
        "p_animal_parent": probs[:, idx["Animal"]],
        "p_animal_max": probs[:, [idx[l] for l in ANIMAL_LABELS]].max(1),
    })
    df.insert(1, "pred_group", df["pred"].map(GROUP_OF))
    if target is not None:
        target = np.asarray(target)
        df["true_score"] = scores[rows, target]
        df["true_rank"] = (scores > df["true_score"].to_numpy()[:, None]).sum(1) + 1
        df["correct"] = df["pred"].to_numpy() == CLASSES[target]
    return df, scores
