# Self Attention Intuition 

Self-attention is a crucial mechanism in modern deep learning models that allows relevant parts of the sequence for each word or token to be identified. We have Query, Key, and Value (Q, K, V) vectors that are derived:
* Q: represents the word in focus
* K: represents each word as a reference to match against
* V: represents the actual information we want to transfer from each word in the sequence

## Mathematical Formulation

The attention scores are computed using the dot product of the Query and Key vectors, scaled by the square root of the dimension of the Key vectors and passed through a softmax function.

\[ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V \]

## Multi-Head Attention

Multi-head attention allows the model to jointly attend to information from different representation subspaces. Instead of performing a single attention function, we perform \( h \) attention functions (or heads) in parallel.

## Code Example

Here is a basic Python implementation of self-attention:

```python
import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=-1, keepdims=True)

def self_attention(Q, K, V):
    d_k = Q.shape[-1]
    scores = np.dot(Q, K.T) / np.sqrt(d_k)
    attention_weights = softmax(scores)
    output = np.dot(attention_weights, V)
    return output, attention_weights

# Example usage
Q = np.array([[1, 0, 1], [0, 1, 0]])
K = np.array([[1, 0, 1], [0, 1, 0]])
V = np.array([[1, 0], [0, 1]])

output, attention_weights = self_attention(Q, K, V)
print("Output:", output)
print("Attention Weights:", attention_weights)
