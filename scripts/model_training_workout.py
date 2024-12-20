import numpy as np

def train_model(X):
    # Initialize weights and biases
    W = np.random.rand(5, 5)
    b = np.random.rand(5, 1)

    # Forward propagation
    Z = np.dot(W, X) + b

    # Softmax activation function
    def softmax(Z):
        exp_Z = np.exp(Z - np.max(Z, axis=0))
        return exp_Z / np.sum(exp_Z, axis=0)

    A = softmax(Z)
    return A
