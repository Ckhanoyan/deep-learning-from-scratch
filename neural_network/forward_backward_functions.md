# Forward and Backward Functions in Deep Neural Network

This diagram I developed, which I learned from Andrew NG's deep learning specialization courses, shows how it processes data (forward propagation) and how it learns (backward propagation). Remember that each layer performs a calculation and then passes the results to the next layer, including adjusting itself through learning. 

While forward and backward propagations are already discussed in the other files, this cache in the diagram is like a memory that stores intermediate values during forward pass. These are later used in the backward pass to speed up learning, but what does that mean? Based on my learning and understanding (so far), this will be also used to calculate gradients. Without cache, the network would have to recompute everything, which may be doable but also ineffective. 

In a situation where the neural network will need to adjust its weights (W) and biases (b) to reduce errors, the network will need information from the forward pass like the pre-activation value, Z[1], and the output from the previous layer. 

### Example / Metaphor 
* Forward pass: you mix ingredients and bake a bake. Z[1] amd A[1] are the intermediate steps like batter before you bake it and then the final baked cake.
* Cache: you write down how much of each ingredient you used
* Backward pass: later, when you taste the cake (error) and want to adjust the recipe. To fix the batter, you need the cached ingredient amounts. Without cached information, you may have to redo the entire recipe.

### Backward pass (bottom section in the diagram)
This is when the network learns by adjusting its weights and biases to reduce errors. 
* Input: gradient (dA[l]) tells the layer how to adjust itself.
* Processes: It uses cached Z[1] to calculate how much to change each weight and biases (dW[l], db[l]). It also computes the gradient (dA[l-1]) to send back to the previous layer.
* Output: Gradients dW[l], db[l], dA[l-1] to adjust the layer and inform the previous layer. 

<img width="700" alt="{D86D6414-C2B0-47C1-A1B2-7238045295FF}" src="https://github.com/user-attachments/assets/c8003888-5189-4cf2-b22e-8e2697df241c" />
