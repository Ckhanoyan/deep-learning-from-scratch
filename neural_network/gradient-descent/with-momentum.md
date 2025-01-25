# What is Gradient Descent with Momentum? 

Momentum helps accelerate gradient descent in the right direction without either going too fast or too slow (vertically), including dampening oscillations. The idea of the whole thing is to have a ball rolling down a hill and gain speed over time, but momentum uses a velocity term to update over time based on past gradients - which allows the algorithm to take more consistent steps in the right direction. 

### Real Life Use Case: Training a NN for Image Classification

Let's use the example of classying dogs vs. cats. Training a neural network involves updating the model's parameters to minimize a loss function using gradient descent. Using momentum helps speed up the convergence, especially when the cost function has noisy gradients. 

For this situation, without momentum, the updates to the parameters may zig-zag, making slow progress. With momentum, the model will remember the past gradients, allowing it to move faster in the correct direction and avoid oscillating. 

<img width="600" alt="{4775401A-5AA1-4EE3-AC8F-08338A9BC1B9}" src="https://github.com/user-attachments/assets/c48c02c9-96fa-49a0-bfab-f164e644806e" />

This momentum helps speed up convergence and smoothens the optimization path and helps overcome zig-zags in the update. This code just demonstrates the basics of gradient descent with momentum applied to a simple cost function, however, it can be used in more complex machine learning tasks. 

Here's the snapshot of the code I did (see the actual code implementation: neural_network/gradient-descent/with-momentum-code.py

<img width="800" alt="{7BED364E-C5F1-4E4B-9CC2-10309A67D631}" src="https://github.com/user-attachments/assets/2ceb6bcd-4471-4611-8fd9-7a6598f63d60" />
