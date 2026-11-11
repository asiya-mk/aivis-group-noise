AI-aided pair:
Asiya Meshitbay K12648788
Rachid Derar K12236997

At the start of Phase 1, I told the LLM to act as a collaborator, not a tool, and to call me out when I slipped. It did, more often than I expected. When I asked it to “complete my code” and choose the label mapping, it wrote defaults but sent the actual decisions back to me: whether hen and rooster may share a label, what to do with classes AudioSet doesn’t cover, whether birds count as animals. That changed how I worked with it for the rest of the phase.

The interesting shift was in how we used it for visualization. Early on, the LLM suggested a confidence threshold to filter out weak predictions, but I didn’t want to hide them, so I decided we should make it a slider in our visualization instead. My partner then built it. The model’s scores turned out to be low overall, so the slider itself became one of our findings..

I also tried to use the LLM as a critic. Before sharing results with the group, I asked it to check my summary against the data. It showed that 443 of the 455 “mistakes” in the mixing experiment were simply the competing sound winning, not real confusions. That changed how we read our confusion matrix and pointed us to the one real weak spot: hen, which loses to rooster in every mix.

Not everything was smooth. When I added imitation and mimicry data, the LLM questioned whether 8 files were enough, and I pushed back. Its code once assumed a file on Drive that only existed on my laptop, and the run crashed. And it wrote most of the perturbation code, so I had to make sure I understood every result I present.

I still find the line between tool and collaborator blurry, but now I notice which side of it I’m on.


AI helped us mainly as a visualization design collaborator. Given the Phase 1 goals and datasets, it proposed concrete chart types that mapped well to the analysis questions a cumulative confidence sweep to show prediction drift, a cross-dataset comparison to show confidence and predicted-family shifts, and a mistakes-only confusion matrix to expose which sound families replaced animal predictions. It also helped with quick implementation of these in Plotly and draft “how to read the chart” explanations and takeaways.

The human role remained central in deciding which suggestions to accept or reject (e.g., rejecting PCA for Phase 1), keeping the scope aligned with final model outputs, and verifying that the reported numbers matched the actual plots. Overall, AI accelerated the chart ideation, implementation, and interpretation, while the human guided relevance and scope.
