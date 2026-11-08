# AI Interaction Log

## Prompts Used
* I explained the Phase 1 goals and the datasets we have (clean animals, noise, mixed audio, imitations, lyrebird).
* I asked the AI to suggest charts to analayze model results and behaviour.
* I asked the AI to help me implement the accepted suggestions.

## AI Suggestions & My Decisions
* **Suggestion:** Make a line chart showing how predictions change when the model is unsure.
  * **Decision: Accepted.** It clearly showed how the model handles background noise compared to adding a second distinct sound.
* **Suggestion:** Add a "Mistakes Only" filter to the confusion matrix and group it by sound type.
  * **Decision: Accepted.** It removed the clutter of correct answers so we could easily see when a background sound (like a siren) tricked the model.
* **Suggestion:** Build a complex scatter plot (PCA) to group the model's outputs.
  * **Decision: Rejected (for Phase 1).** It looked too much like we were looking inside the model to see how it works, which is meant for Phase 2. I saved it for the December deadline.

## Failure Patterns & Best Practices
* **Failure Pattern:** The AI could not read raw data files when I pasted them directly into the chat as text.
* **Best Practice:** Showing the AI screenshots of the actual charts alongside the code got much better, more useful answers.