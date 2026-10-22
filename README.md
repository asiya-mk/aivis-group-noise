# aivis-group-noise — AI & Visualization Lab WS26 — Sound Recognition (VIS4AI + AI4VIS)

Group project for the JKU *AI and Visualization* lab: using visualization to explain a
pre-trained sound recognition model and diagnose its failure modes.

- **Phase I – How does the model behave?** Black box: visualize patterns between input audio and model output (errors, confidence shifts under perturbations, counterfactuals).
- **Phase II – What did the model learn?** Open box: attention / saliency over spectrograms, layer embeddings — used to *explain* Phase I findings.
- **AI4VIS:** one pair works with generative AI, the other without; pairs swap between phases. We log prompts and decisions.

## Model & dataset


## Team & pairs

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
notebooks/   one notebook per person/task, named NN_initials_topic.ipynb
src/         shared code (paths, model loading, prediction, perturbations)
results/     small CSV outputs (< a few MB)
figures/     exported plots for report/presentation
ai_log/      AI4VIS log template
docs/        meeting notes
```

2. shared Google Drive folder :
Audio data, perturbed audio, large results 
Link: https://drive.google.com/drive/folders/10wj1_zowv9ZjvUMIf7q7ltezllEfGiwc?usp=drive_link

3. Shared Google Sheet in the Drive folder 
AI4VIS prompt log
(template: `ai_log/ai_log_template.csv`) |

## Working in Colab

1. Open the Drive folder once and choose **"Add shortcut to Drive"** (otherwise Colab cannot see it).
2. Start from `notebooks/00_setup_colab.ipynb` — it mounts Drive, clones this repo and creates the data folders.
3. To push from Colab, use a GitHub personal access token (never commit it), or download the notebook and commit locally.

## Rules

- WE DONT WRITE OVER EACH OTHER IN 1 NOTEBOOK. Either different branches ot different notebooks so we can experiment with model seperately.
- No audio or model weights in git — they go to Drive (`.gitignore` blocks them).
- Whoever uses GenAI logs the important prompts .
