# aivis-group-noise — AI & Visualization Lab WS26 — Sound Recognition (VIS4AI + AI4VIS)

Group project for the JKU *AI and Visualization* lab: using visualization to explain a
pre-trained sound recognition model and diagnose its failure modes.

- **Phase I – How does the model behave?** Black box: visualize patterns between input audio and model output (errors, confidence shifts under perturbations, counterfactuals).
- **Phase II – What did the model learn?** Open box: attention / saliency over spectrograms, layer embeddings — used to *explain* Phase I findings.
- **AI4VIS:** one pair works with generative AI, the other without; pairs swap between phases. We log prompts and decisions.

## Model & dataset
Task
For our project we want to look at environmental sound classification, mainly the question of whether a model can tell animal sounds apart from other kinds of sounds. We are interested in which sounds get mixed up with each other, both inside the animal group (e.g. hen vs. rooster) and between animal and non-animal sounds. In Phase I we treat the model as a black box and look at its errors, confusions, confidence and how it reacts to changed inputs (noise, volume, mixing clips). In Phase II we want to look inside the model and check what happens in its internal representations for the confusions we found.

Model
Model: We use the Audio Spectrogram Transformer (AST), the pretrained checkpoint MIT/ast-finetuned-audioset-10-10-0.4593 from Hugging Face. AST turns an audio clip into a spectrogram (an image of the sound), cuts it into small patches and processes them with a Vision Transformer, so it works without convolutions. This checkpoint was trained on AudioSet and predicts 527 sound labels. Since our dataset has different classes, we plan to map the AudioSet labels to our dataset classes. We might fine-tune the model later if we need it for Phase II, but we do not plan on it at the start.
https://huggingface.co/docs/transformers/model_doc/audio-spectrogram-transformer 

Dataset: Our main dataset is ESC-50 (ashraq/esc50 on Hugging Face). It has 2,000 clips of 5 seconds each, 50 sound classes in 5 categories (animals, natural soundscapes, human non-speech sounds, domestic sounds and urban noises) and 5 predefined folds. We will use all categories so we can compare animal and non-animal sounds. We might use additional dataset for expanding our search if needed.



## Team & pairs
AI added in phase 1
Asiya, Rachid

Himan only in phase 1
Gurmehak, Elif

## Timeline

| Date       | Milestone |
| 21.10.2026 | Group registered |
| 28.10.2026 | Model & task registered on Moodle |
| 11.11.2026 | Midpoint deadline | 
| 09.12.2026 | Final deadline, then presentations  |


## Where things live
1. This repo:
Code, notebooks, small CSVs, figures    

```
notebooks/   one notebook per person
src/         shared code 
results/     small CSV outputs (< a few MB)
figures/     exported plots for report/presentation
ai_log/      AI4VIS logs
docs/        meeting notes
```

2. shared Google Drive folder :
Audio data, perturbed audio, large results 
Link: https://drive.google.com/drive/folders/10wj1_zowv9ZjvUMIf7q7ltezllEfGiwc?usp=drive_link

3. Shared Google Sheet in the Drive folder 
AI4VIS prompt log
## Working in Colab

1. Open the Drive folder once and choose **"Add shortcut to Drive"** (otherwise Colab cannot see it).
2. Start from `notebooks/00_setup_colab.ipynb` — it mounts Drive, clones this repo and creates the data folders.
3. To push from Colab, use a GitHub personal access token. 
For now it's for VS + collab extension use so we don't accidently commit tokens. You’d need to enter it each time the runtime restarts. You might save tocken locally but be aware of not sharing it by accident

## Rules

- WE DONT WRITE OVER EACH OTHER IN 1 NOTEBOOK. Each use their own
- No audio or model weights in git — they go to Drive (`.gitignore` blocks them).
- Whoever uses GenAI logs the important prompts .
