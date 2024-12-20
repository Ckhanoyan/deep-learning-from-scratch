
    import numpy as np

    # Sigmoid function
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    # Loss function: Binary cross-entropy
    def compute_loss(y, predictions):
        m = len(y)  # Number of examples
        loss = -1/m * (np.dot(y, np.log(predictions)) + np.dot((1 - y), np.log(1 - predictions)))
        return loss

    # Gradient calculation
    def compute_gradient(X, y, predictions):
        m = len(y)  # Number of examples
        gradient = (1/m) * np.dot(X.T, (predictions - y))
        return gradient

    # Gradient descent
    def gradient_descent(X, y, weights, learning_rate, iterations):
        for i in range(iterations):
            # Compute predictions
            logits = np.dot(X, weights)
            predictions = sigmoid(logits)

        # Compute loss
        loss = compute_loss(y, predictions)

        # Compute gradient
        gradient = compute_gradient(X, y, predictions)

        # Update weights
        weights -= learning_rate * gradient

        # Print progress
        if i % 100 == 0:
            print(f"Iteration {i}, Loss: {loss:.4f}")

    return weights

    # Example data (Age, BMI)
    applicants = np.array([[25, 22], [30, 28], [35, 26], [40, 24], [45, 30]])
    labels = np.array([1, 0, 1, 0, 1])  # Approval labels (1: Approved, 0: Denied)

    # Normalize features
    applicants_normalized = (applicants - applicants.mean(axis=0)) / applicants.std(axis=0)

    # Add bias term (intercept)
    X = np.hstack((np.ones((applicants_normalized.shape[0], 1)), applicants_normalized))
    y = labels

    # Initialize weights
    weights = np.random.randn(X.shape[1]) * 0.01

    # Hyperparameters
    learning_rate = 0.1
    iterations = 1000

    # Train the model
    final_weights = gradient_descent(X, y, weights, learning_rate, iterations)

    # Final predictions
    final_logits = np.dot(X, final_weights)
    final_probabilities = sigmoid(final_logits)

    # Print results
    print("Final weights:", final_weights)
    print("Final probabilities:", final_probabilities)
