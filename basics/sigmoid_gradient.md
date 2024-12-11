# Calculate the Gradient for the Sigmoid Function Using Health Insurance Approval Prediction 

Why is gradient important for health insurance? In health insurance, decisions are often complex, involving multiple factors like age, income, health history, etc. The gradient plays a role in automating and improving decisions by:
* Optiminzing predictions, e.g., how much BMI matters compared to age
* Reducing human bias
* Handling complexity, e.g., handling large datasets with many factors
* Adaptability

## First, What is the Gradient "Bowl"?

Imagine you are standing on a large, smooth hill shapred like a bowl. At the very bottom of the bowl, that is your treasure chest that represents the best solution to a problem such as the most accurate model for predicting health insurance approval. Your goal is to reach the treasure by walking downhill, and I know that sounds weird. So, the surface of the bowl represents the loss function or how bad your current solution is. Your current position (weights) determines how high or low you are on the bowl. Therefore, each step you take downhill is guided by the GRADIENT, which tells you which direction is steepest. In the other words, as you continue stepping downhill, you are gradually adjusting your weights and making better predictions, including reducing the loss. 

We would use it during backpropagation for logistic regression. Remember the sigmoid function below: 

    σ(x)= 1 / (1 + np/exp(-x))
​
Here is the gradient of sigmoid function, which this formula leverages the property of the sigmoid function to simplify computation. 

    σ'(x) = σ(x) ⋅ (1−σ(x))

Compute the gradient for each input so if we want to find Ypred (Y prediction) coming from (z = Xw + b, the weighted input: 

    σ′(z) = y_pred * (1 - y_pred) 

If we are calculating gradients for logistic regression, we should calculate the gradient of the loss function as well. 

    Loss = -(1/N) * Σ [y_i * log(y_pred) + (1 - y_i) * log(1 - y_pred)]

With above, you will find Error from this formula:

    error = y_pred - y_true

### Health Insurance Approval Prediction 

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

### Key Notes from the Code Above 

* Age and BMI are adjusted to ensure they are on the same scale, making the model learn more effectively
* Adding a Bias Term is a constant value that helps the model account for a baseline approval rate
* Initializing weights is important because the model starts with random numbers (weights) to figure out the relationship between age, BMI, and approval
* The model multiples age and BMI with their respective weights and adds the bias
* The result is passed through a sigmoid function, which converts the numbers into probabilities like "This guy has a 70% chance of approval"
* To measure error (loss), the binary cross-entropy loss tells us how far off the model's predictions are from the true approval labels (lower loss = better predictions)
* To calculate the gradient, we need to measure how much each weight contributes to the error, e.g., the age weight causing high error so the gradient for age will be large and it needs to be adjusted
* To update the weights, the model updates the weights step by step to reduce error, and it is called gradient descent to ensure the model learns the best weights to make accurate predictions
