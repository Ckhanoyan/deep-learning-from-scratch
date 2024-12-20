  import numpy as np

    # Number of features: 5 (Age, Weight, Fitness Level, Goal, Time)
    # Number of examples: 1000 users
    np.random.seed(42)
    X = np.random.rand(5, 1000)  # Input matrix (n_x, m)

    # Initialize weights and biases
    W = np.random.rand(5, 5)     # Weight matrix (5 classes, 5 features)
    b = np.random.rand(5, 1)     # Bias term (5 classes, 1 bias per class)

    # Forward propagation
    Z = np.dot(W, X) + b  # Linear combination

    # Softmax activation function
    def softmax(Z):
        exp_Z = np.exp(Z - np.max(Z, axis=0))  # Numerical stability
        return exp_Z / np.sum(exp_Z, axis=0)

    A = softmax(Z)  # Predicted probabilities for 5 workout types

    print("Shape of predicted probabilities:", A.shape)
    print("Example probabilities for first user:", A[:, 0])
