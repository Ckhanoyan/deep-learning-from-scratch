# Regularization for Neural Network

Imagine that you are packing a suitcase for a trip. Without regularization, you may overpack with things that you do not need for your trip. Regularization is like setting a weight limit for your suitcase (up to 50 lbs for most airports). You only focus on the essentials. So, the neural network focuses on the most important patterns in the data. 

### Frobenius Norm in Neural Network Regularization

The Frobenius norm is an extension of the L2 norm to matrices and is often used for weight matrices in neural networks. 

* L is the orginial loss function
* W is the weight matrix of a layer in the network
* λ is the regularization parameter that controls the trade-off between the original loss and the penalty term

When we apply Frobenius norm regularization, this means we will add it, λ∥W∥ 2 f, to the total loss. 
