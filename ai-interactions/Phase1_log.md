# AI Interaction Log (AI4VIS) 

## Important Prompts Used
* Asked the AI to act as a collaborator, not a tool, and to point it out when I used it as a tool.
* Shared the task, model and dataset, and asked for next steps and for options to map the 527 AudioSet labels to the 50 ESC-50 classes.
* Asked to add perturbations and mixing.
* Asked the AI to check my summary of the results before sharing it with the group.

## AI Suggestions & Decisions

* **Suggestion:** Map AudioSet to ESC-50 with a few specific labels per class instead of the top-1 label.
  * **Decision:** **Accepted.** The top-1 label was often a generic one ("Animal", "Vehicle"), so dog clips came out as "Animal". With specific labels the model gets 80% of all classes right.

* **Suggestion:** Each AudioSet label belongs to only one class (hen = "Cluck", rooster = "Crowing").
  * **Decision:** **Accepted.** If hen and rooster shared a label, their mix-ups would come from our mapping, not from the model.

* **Suggestion:** Keep the 3 classes AudioSet has no label for (drinking_sipping, can_opening, washing_machine) and mark them with a flag.
  * **Decision:** **Accepted.** We can report accuracy with and without them.

* **Suggestion:** The baseline doesn't support our question: animals are 99% correct on clean data, so we need perturbations and mixing to find confusions.
  * **Decision:** **Refined.** I added perturbations and mixing, and also my own idea: lyrebird recordings and humans imitating animals.

* **Suggestion:** Decide whether chirping_birds and crickets count as animals (ESC-50 puts them under "natural").
  * **Decision:** **Rejected.**

* **Suggestion:** Measure "animal-ness" in two ways, because the model's general "Animal" label disagrees with its own animal labels (cow: "Animal" 0.01, "Moo" 0.89).
  * **Decision:** **Accepted.** Good idea for later, we keep both scores for Phase II.

* **Suggestion:** 8 imitation files are too few to generalise.
  * **Decision:** **Refined.** I kept the imitation data but present it as first observations, not conclusions.

* **Suggestion:** Check my summary against the result files before sharing it.
  * **Decision:** **Refined.** I used the corrected summary. The AI showed that most mixing "mistakes" were just the competing sound winning. I checked the lyrebird "frog" predictions by listening: in XC738172 the lyrebird really imitates a frog.

* **Suggestion:** Use a confidence threshold to filter out low-confidence predictions (e.g. a bird whistle scored as chirping_birds at 0.0065).
  * **Decision:** **Refined.** I didn't want to hide these predictions, so we made the threshold a slider in the visualization instead.

## Failure Patterns
* The AI's experiment script loaded a file that only existed on my laptop, so the run in Colab crashed. The AI fixed it after I sent the error.
* The AI wrote most of the perturbation code, so I had to make sure I understood every result I present.
