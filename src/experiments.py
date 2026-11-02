import io
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import librosa
from datasets import load_dataset, Audio
from tqdm.auto import tqdm

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.paths import BIG_RESULTS_DIR, DATA_DIR, RESULTS_DIR, ensure_dirs
from src.esc import CLASSES, SR, load_model, predict, prediction_table
from src import perturb

SNR_DB = [20, 10, 5, 0, -5, -10]
GAIN_DB = [-40, -30, -20, -10, 10]
MIX_DB = [10, 5, 0, -5, -10]
DISTRACTORS = ["siren", "engine", "rain", "crying_baby"]
PARTNER = {
    "dog": "cat", "cat": "dog", "rooster": "hen", "hen": "rooster", "cow": "sheep", "sheep": "cow",
    "pig": "cow", "frog": "insects", "insects": "crickets", "crow": "chirping_birds",
}
CLIPS_PER_CLASS = 4


def run_files(fe, model, labels, folder):
    rows, waves = [], []
    for path in sorted(folder.glob("*")):
        if path.suffix.lower() not in {".wav", ".mp3", ".flac", ".ogg"}:
            continue
        y = perturb.load_audio(path)
        chunks = perturb.windows(y) if len(y) > 5 * SR else [(0.0, y)]
        for t, w in chunks:
            rows.append({"file": path.name, "t_start": t, "rms": perturb.rms(w)})
            waves.append(w)
    if not waves:
        return None, None
    probs = predict(fe, model, waves)
    table, _ = prediction_table(probs, labels)
    top5 = [", ".join(f"{labels[j]} {p[j]:.2f}" for j in np.argsort(p)[::-1][:5]) for p in probs]
    return pd.concat([pd.DataFrame(rows), table], axis=1).assign(top5_audioset=top5), probs


def esc_waves():
    ds = load_dataset("ashraq/esc50", split="train").cast_column("audio", Audio(decode=False))
    meta = ds.remove_columns("audio").to_pandas()
    load = lambda i: librosa.load(io.BytesIO(ds[int(i)]["audio"]["bytes"]), sr=SR)[0]
    return meta, load


def pick_clips(meta, labels):
    base, _ = prediction_table(np.load(BIG_RESULTS_DIR / "baseline_probs.npy"), labels, meta["target"])
    meta = meta.assign(correct=base["correct"], conf=base["conf"])
    targets = meta[(meta["target"] < 10) & meta["correct"]]
    targets = targets.groupby("category", group_keys=False).apply(
        lambda g: g.sample(min(CLIPS_PER_CLASS, len(g)), random_state=0))
    # cleanest distractor per class: correctly classified with the highest confidence
    needed = set(DISTRACTORS) | set(PARTNER.values())
    others = meta[meta["category"].isin(needed) & meta["correct"]].sort_values("conf", ascending=False)
    others = others.rename_axis("row").reset_index().drop_duplicates("category").set_index("category")
    return targets, others


def run_perturbations(fe, model, labels):
    meta, load = esc_waves()
    targets, others = pick_clips(meta, labels)
    other_wave = {c: load(i) for c, i in others["row"].items()}
    rows, waves = [], []
    for i, r in targets.iterrows():
        y = load(i)
        base = {"filename": r["filename"], "category": r["category"], "target": r["target"]}
        rows.append({**base, "experiment": "clean", "param": 0.0}); waves.append(y)
        for snr in SNR_DB:
            rows.append({**base, "experiment": "noise", "param": snr}); waves.append(perturb.add_noise(y, snr, seed=i))
        for g in GAIN_DB:
            rows.append({**base, "experiment": "gain", "param": g}); waves.append(perturb.gain(y, g))
        for other in DISTRACTORS + [PARTNER[r["category"]]]:
            for ratio in MIX_DB:
                rows.append({**base, "experiment": "mix", "param": ratio, "distractor": other,
                             "distractor_file": others.loc[other, "filename"]})
                waves.append(perturb.mix(y, other_wave[other], ratio))
    probs = np.concatenate([predict(fe, model, waves[s:s + 64]) for s in tqdm(range(0, len(waves), 64))])
    table, _ = prediction_table(probs, labels, [r["target"] for r in rows])
    return pd.concat([pd.DataFrame(rows), table], axis=1), probs


if __name__ == "__main__":
    ensure_dirs()
    fe, model, labels = load_model()
    for name in ["lyrebird", "imitations"]:
        df, probs = run_files(fe, model, labels, DATA_DIR / name)
        if df is None:
            print(f"no audio in {DATA_DIR / name}, skipped")
            continue
        df.to_csv(RESULTS_DIR / f"{name}_predictions.csv", index=False)
        np.save(BIG_RESULTS_DIR / f"{name}_probs.npy", probs)
        print(name, len(df), "windows")
    if "--skip-esc" not in sys.argv:
        df, probs = run_perturbations(fe, model, labels)
        df.to_csv(RESULTS_DIR / "perturbation_predictions.csv", index=False)
        np.save(BIG_RESULTS_DIR / "perturbation_probs.npy", probs)
        print("perturbations", len(df), "rows")
