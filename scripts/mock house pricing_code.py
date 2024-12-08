import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate mock data
# Number of samples
num_samples = 100

# Features: bedrooms, bathrooms, square footage
bedrooms = np.random.randint(1, 6, num_samples)       # 1 to 5 bedrooms
bathrooms = np.random.randint(1, 5, num_samples)      # 1 to 4 bathrooms
sq_ft = np.random.randint(500, 3500, num_samples)     # 500 to 3500 sq ft

# True weights for generating prices
true_weights = np.array([50, 30, 0.1])  # Coefficients for bedrooms, bathrooms, sq_ft
noise = np.random.randn(num_samples) * 1000  # Random noise for realism

# Compute the true prices
true_prices = (
    bedrooms * true_weights[0] +
    bathrooms * true_weights[1] +
    sq_ft * true_weights[2] +
    noise
)

# Combine features into a single dataset
X = np.vstack([bedrooms, bathrooms, sq_ft]).T  # Feature matrix
y = true_prices  # Target prices

# Step 2: Initialize weights and bias randomly
weights = np.random.randn(3)  # For 3 features
bias = np.random.randn()

# Step 3: Train the model using gradient descent
def predict(X, weights, bias):
    """Linear model prediction."""
    return np.dot(X, weights) + bias

def compute_loss(y_true, y_pred):
    """Mean Squared Error loss."""
    return np.mean((y_true - y_pred) ** 2)

def gradient_descent(X, y, weights, bias, learning_rate, epochs):
    """Perform gradient descent to optimize weights and bias."""
    n = len(y)  # Number of samples
    losses = []  # Store losses for visualization

    for epoch in range(epochs):
        # Predictions
        y_pred = predict(X, weights, bias)

        # Compute gradients
        error = y_pred - y
        dW = (1 / n) * np.dot(X.T, error)  # Gradient for weights
        dB = (1 / n) * np.sum(error)      # Gradient for bias

        # Update weights and bias
        weights -= learning_rate * dW
        bias -= learning_rate * dB

        # Compute and store loss
        loss = compute_loss(y, y_pred)
        losses.append(loss)

        # Print progress every 10 epochs
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {loss:.2f}")

    return weights, bias, losses

# Training parameters
learning_rate = 0.0000001
epochs = 100

# Train the model
weights, bias, losses = gradient_descent(X, y, weights, bias, learning_rate, epochs)

# Step 4: Visualize the training loss
plt.figure(figsize=(10, 6))
plt.plot(losses, label="Training Loss", color="blue")
plt.title("Loss During Training", fontsize=16)
plt.xlabel("Epoch", fontsize=14)
plt.ylabel("Mean Squared Error Loss", fontsize=14)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.show()

# Step 5: Display final weights and make predictions
print("\nFinal Weights:", weights)
print("Final Bias:", bias)

# Predict for a new house
new_house = np.array([3, 2, 1500])  # 3 bedrooms, 2 bathrooms, 1500 sq ft
predicted_price = predict(new_house, weights, bias)
print("\nPredicted Price for New House (3 bed, 2 bath, 1500 sq ft):", predicted_price)
