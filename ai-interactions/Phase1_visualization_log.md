# AI Interaction Log (AI4VIS)

## Important Prompts Used
* Provided an overview of the Phase 1 goals and the available datasets (clean animals, noise, mixed audio, human imitations, lyrebird).
* Asked the AI to suggest specific visualizations to analyze confidence thresholds and model robustness.
* Prompted the AI to implement the suggested visualizations using Plotly.

## AI Suggestions & Decisions

* **Suggestion:** Create a Cumulative Confidence Sweep (line chart) showing prediction drift as confidence drops.
  * **Decision:** **Accepted.** This directly answered the assignment prompt regarding "errors/confidence change".

  ![Cumulative Confidence Sweep](../viz_plots/cumulative_confidence_sweep_urban_human_animal.png)

  **How to read the chart:**
  * **X-axis:** Represents the confidence threshold.
  * **Y-axis:** Shows the percentage of true animal clips predicted as a specific category.

  **We have three conditions:**
  * **Clean Baseline (in green):** Represents predictions on the original, unmodified animal recordings with no added sounds.
  * **White Noise (in yellow):** Just static background noise. It has no specific meaning (it doesn't sound like an animal, a person, or a vehicle).
  * **Mixed Audio (in red):** Where we take the animal sound and mix it with a distinct competing sound, like a siren or a crying baby.

  **Graph 1: % Predicted as URBAN**
  Starting with the leftmost graph, we look at how often the model wrongly guesses an Urban sound. The Clean Baseline in green is completely flat at 0%, meaning the model never confuses a pristine animal sound for a city sound. The White Noise in yellow starts around 10% on the left and drops below 5%. This tells us that while the generic static causes minor confusion in the hardest clips, the model mostly sees through it. However, the Mixed Audio in red spikes to over 22%. Because we mixed the animal sounds with urban distractors like sirens or engines, the model gets hijacked. Instead of hearing the animal, it confidently guesses the background noise.

  **Graph 2: % Predicted as HUMAN**
  Moving to the middle graph, we look at Human predictions. Again, the Clean Baseline in green is perfectly flat at 0%. The White Noise in yellow is also near 0%, which makes sense because generic static doesn't sound like a human voice. But looking at the Mixed Audio in red, at the lowest confidence threshold where the model is most confused, the percentage of animal clips misclassified as human starts at roughly 50%. This happens because we mixed the animal audio with human distractors, like a crying baby. The competing sound overwhelms the model, causing it to abandon the animal prediction entirely. The line only drops as we include higher-confidence clips where the animal sound was louder.

  **Graph 3: % Predicted as ANIMAL**
  Finally, the rightmost graph shows us the correct predictions. The Clean Baseline in green is a perfect, flat line at 100%. The White Noise in yellow starts around 82% and rises to 95%. Even when static makes the model unsure, it still knows the core signal is an animal. But the Mixed Audio in red is startling. On the far left, it starts at 0%. This means that for the most confusing mixed clips, the competing background sound entirely erases the animal's identity. The model only recovers to about 65% as we move to the right and include the clips where the animal sound was clear enough to overpower the distractor.

  These plots show that when we add generic static, the model gets a little unsure but stays mostly correct. But when we mix in a meaningful background sound, the model loses confidence as it is influenced by the distractor. It abandons the animal prediction and misclassifies the audio as a human or urban sound.

* **Suggestion:** Create a Cross-Dataset Comparison chart comparing animal confidence distributions and predicted sound families across clean animals, white noise, mixed audio, human imitations, and lyrebird mimicry.
  * **Decision:** **Accepted.** It provides a clear side-by-side overview of how confidence and predicted sound families shift across all five datasets.

  ![Cross-Dataset Comparison](../viz_plots/cross_dataset_comparison_confidence_and_sound_families.png)

  **How to read the chart:**
  The left graph shows the distribution of the model's confidence scores (from 0 to 1) for animal sounds. The right graph shows the share of predicted sound families (from 0% to 100%) for each condition.

  **We have five conditions:**
  * **Clean Animals:** The original, unmodified animal recordings with no added sounds.
  * **White Noise:** The animal sounds with added generic static.
  * **Mixed Audio:** The animal sounds mixed with a distinct competing sound, like a siren or a crying baby.
  * **Human Imitations:** A human trying to mimic an animal sound.
  * **Superb Lyrebird:** Recordings of a bird known for mimicking other sounds.

  **Graph 1: Animal Confidence Score Distribution (Left Graph)**
  Starting with the left graph, the boxplots show how sure the model is that the audio belongs to an animal. For Clean Animals, the box is high up, meaning the model is generally very confident. White Noise and Mixed Audio show wider boxes, indicating the model's confidence varies depending on the specific clip. Human Imitations have the lowest confidence, with the box sitting near 0, meaning the model rarely thinks an animal is present. Superb Lyrebird shows moderate confidence, sitting lower than the clean baseline.

  **Graph 2: Share of Predicted Sound Families (Right Graph)**
  Moving to the right graph, the stacked bars show what the model actually guessed. For Clean Animals, the bar is predominantly green, meaning it correctly predicts an animal. White Noise remains mostly green as well, showing the model handles static well. However, looking at Mixed Audio, the green portion drops to 64%, with predictions shifting into urban, human, and natural sounds. For Human Imitations, the green drops to 70%, and the purple section (Human Sounds) increases to 25%, as the model detects the human voice. Finally, for the Superb Lyrebird, the green drops to roughly 12%, and the model predominantly predicts Natural Sounds (blue) at 84%.

  **Conclusion:**
  These plots show that the model is highly confident and accurate with clean audio and generic static. However, when presented with meaningful distractors such as mixed audio, human imitations, or lyrebird mimicry, the model's confidence drops, and its predictions shift away from the animal category.

* **Suggestion:** A confusion matrix grouped by sound family, filtered to show only mistakes.
  * **Decision:** **Accepted.** It hid the correct answers so we could easily see exactly when a background sound tricked the model (like guessing a siren instead of a dog).

  ![Confusion Matrix — Mistakes Only](../viz_plots/confusion_matrix_perturbed_animals_conf_le_0.88_mistakes_only.png)

* **Suggestion:** Build a 2D scatter plot (PCA) to map the model's outputs.
  * **Decision:** **Rejected (for Phase 1).** It involves looking at the model's internal workings rather than just its final outputs.
