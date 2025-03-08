# ragtube
Simple ollama RAG agent to summarize EwwwTube videos

## Examples

- Initial pull of transcript with summary

```default
> python ragtube.py zYzLOE-E-xw
fetching transcript...
retrieved transcript - starting summarization with llama3:latest...

summary:
The video transcript is about building a raised garden bed using metal and wood. The host starts by building a frame for the bed using metal squares and wooden boards. They then fill the bed with logs, branches, and twigs to save money on soil. Next, they add lawn waste and leaves to help break down the organic matter. Finally, they top it off with a layer of garden soil and homemade compost.

The host emphasizes that using this method is not only cost-effective but also helps reduce waste by repurposing materials found in their yard. They also suggest making your own compost or using store-bought black cow manure to add nutrients to the soil.

Overall, the video demonstrates an easy and relatively inexpensive way to build a raised garden bed using sustainable materials.
>
```

- Continued chat in context (untested)

```default
> summarize the steps to build a raise bed garden from the video
llama3: Based on the video transcript, here are the steps to build a raised bed garden:

1. Build the frame:
	* Use metal squares as the base of the bed.
	* Add wooden boards to create the sides and top of the bed.
2. Fill the bed with organic matter:
	* Start by filling the bed with logs, branches, and twigs from your yard or nearby woods.
3. Add lawn waste and leaves:
	* Once the bed is filled with larger limbs, add a layer of lawn waste and leaves to help break down the organic matter.
4. Top it off with soil:
	* Fill the bed with a nice layer of garden soil (not just topsoil) to provide good drainage and nutrient-rich soil for your plants.
5. Add compost:
	* Use homemade compost or store-bought black cow manure to add nutrients to the soil and promote healthy plant growth.

That's it! By following these steps, you can create a raised bed garden that is both sustainable and cost-effective.
```
