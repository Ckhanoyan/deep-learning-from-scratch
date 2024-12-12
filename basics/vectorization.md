# Vectorization 

### Vectorization is critical in deep learning that everybody should know about.

It is a technique in programming where operations are performed on entire arrays or vectors of data, rather than using loops to process individual elements. I was asked to compare both non-vectorized example and vectorized example so here is what I learned. 

## Non-Vectorized Example Using Loops 

We are not using numpy but only import math. 

    import math 

    # logits for multiple examples 
    logits = [[2.5, 1.2, 0.3], [1.0, 2.0, 0.5]] # two sets of logits 

    softmax_results = []

    # apply softmax for each set of logits using loops 
    for logits in logits: 
      exp_logit = [math.exp(x) for x in logit]    # exponentiate each element 
      sum_exp = sum(exp_logit)    # sum of exponentials 
      probabilities = [x / sum_exp for x in exp_logit]   # normalize
      softmax_results.append(probabilities)

    print("Softmax Results (Non-Vectorized): ", softmax_results)

## Vectorized Example Using NumPy

    import numpy as np

    # Logits for multiple examples
    logits = np.array([[2.5, 1.2, 0.3], [1.0, 2.0, 0.5]])  # Two sets of logits

    # Apply softmax using vectorized operations
    exp_logits = np.exp(logits)  # Exponentiate entire array
    sum_exp_logits = np.sum(exp_logits, axis=1, keepdims=True)  # Sum along rows
    softmax_results = exp_logits / sum_exp_logits  # Normalize

    print("Softmax Results (Vectorized):")
    print(softmax_results)

## Ok... But why is it important?

Vectorized operations are faster than loops because they utilize low-level code, and this can help save time for large datasets. For readability, vectorized code is much cleaner to understand such as above. We can also leverage hardware because vectorized code can take advantage of modern hardware optimizations like SIMD or GPU acceleration.
