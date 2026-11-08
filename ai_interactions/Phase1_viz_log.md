# AI Interaction Log (AI4VIS)

## Important Prompts Used
* Provided an overview of the Phase 1 goals and the available datasets (clean animals, noise, mixed audio, human imitations, lyrebird).
* Asked the AI to suggest specific visualizations to analyze confidence thresholds and model robustness.
* Prompted the AI to implement the suggested visualizations using Plotly.

## AI Suggestions & Decisions

* **Suggestion:** Create a Cumulative Confidence Sweep (line chart) showing prediction drift as confidence drops.
  * **Decision:** **Accepted.** This directly answered the assignment prompt regarding "errors/confidence change" and clearly showed the impact of mixed audio versus white noise.
* **Suggestion:** Use a "Mistakes Only" filter on the confusion matrix grouped by semantic hierarchy.
  * **Decision:** **Accepted.** It removed visual noise from correct predictions and clearly isolated the distractor hijacking behavior (e.g., dog -> siren).
* **Suggestion:** Implement a 2D PCA projection of the behavioral space.
  * **Decision:** **Rejected (for Phase 1).** While analytically correct, visualizing a projection looks too much like analyzing internal representations (opening the "black box"), which is strictly a Phase 2 requirement. This was saved for the December submission.

## Failure Patterns & Best Practices
* **Failure Pattern:** The AI struggled to interpret raw binary `.npy` data pasted directly into the chat interface.
* **Best Practice:** Providing the AI with screenshots of the rendered Plotly dashboards alongside the Jupyter Notebook code yielded much better, context-aware feedback.