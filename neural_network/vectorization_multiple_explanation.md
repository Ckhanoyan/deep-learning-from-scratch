# Understanding Vectorization in Neural Networks

<img width="800" alt="{D8A33A38-6005-439F-820B-3217F1C8C2BF}" src="https://github.com/user-attachments/assets/7e549d32-42c1-4fff-8c92-b13f79630eee" />

I made the similar drawing from deeplearning.ai coursea, and this image above basically shows how we should compute outputs in a neural network for multiple examples by using vectorization. In the other words, we are just operating on an entire dataset or batch at once instead of processing one example at a time or doing a loop for each example. 

Remember the neural network diagram that represents inputs (features), layers (neurons with weights and biases)m and output (predicted value). 

### Layer 1 (top right)
For top right in the picture processing one example (Layer 1), 
* we compute weighted sum, using Z[1] (i) = W[1]x(i) + b[1]
* We then apply activiation, using a[1] (i) = σ(z[1] (i))

### Layer 2 (top right)
We repeat with activations from the previous layer, 
* z[2] (i) = W [2] a [1] (i) + b [2]
* a [2] (i) = σ (z [2] (i) )

This loop above is considered slow as we are only repeating this process for all m examples in a loop. 

### Vectorized Approach (Bottom Right) Using Matrix Operations

For Layer 1, we combine all m examples into a single matrix X. 
* To combine all m examples, do this, X = [ x(1), x(2), ... , x(m)]

* Compute the weighted sum for all m examples at once, do this, Z[1] = W [1] X + b [1]
* Where Z[1] contains one column per example

* Apply activation for all examples simultaneously: A[1] = σ(Z[1])

* Layer 2, we repeat with outputs from the previous layer:
* Z[2] = W [2] A [1] + b [2]
* A [2] = σ (Z[2])

### Key Takeaways 

I am not 100% confident understanding the whole process, but I think I understand the concept. As long as I understand the flow from input to weighted sum to activation to repeat, I think that is important to know. In addition, vectorization is critical for scaling neural networks to large datasets where there may be so many examples.

I will start doing some small neural networks using libraries such as NumPy and maybe some code examples.

### Python Implementation Step by Step
See my code practice link here: 
[vectorization_multipleexamples.py](https://github.com/Ckhanoyan/deep-learning-from-scratch/blob/main/scripts/vectorization_multipleexamples.py)

### Learning Resources
* https://www.coursera.org/learn/machine-learning

