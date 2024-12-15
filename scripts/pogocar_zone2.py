import numpy as np

# Step 1: Initialize parameters
def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(42)  # For reproducibility
    W1 = np.random.randn(input_size, hidden_size) * 0.01  # Input to hidden
    b1 = np.zeros((1, hidden_size))                      # Bias for hidden
    W2 = np.random.randn(hidden_size, output_size) * 0.01  # Hidden to output
    b2 = np.zeros((1, output_size))                     # Bias for output
    return W1, b1, W2, b2

# Step 2: Forward propagation
def forward_propagation(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1   # Linear step for hidden layer
    A1 = np.maximum(0, Z1)    # ReLU activation
    Z2 = np.dot(A1, W2) + b2  # Linear step for output
    return Z1, A1, Z2

# Step 3: Loss function
def compute_loss(Y_pred, Y):
    m = Y.shape[0]  # Number of examples
    loss = (1 / m) * np.sum((Y_pred - Y) ** 2)
    return loss

# Step 4: Backpropagation
def backward_propagation(X, Y, Z1, A1, Z2, W2):
    m = X.shape[0]  # Number of examples
    dZ2 = (Z2 - Y)  # Error in output
    dW2 = (1 / m) * np.dot(A1.T, dZ2)
    db2 = (1 / m) * np.sum(dZ2, axis=0, keepdims=True)
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * (Z1 > 0)  # Backprop through ReLU
    dW1 = (1 / m) * np.dot(X.T, dZ1)
    db1 = (1 / m) * np.sum(dZ1, axis=0, keepdims=True)
    return dW1, db1, dW2, db2

# Step 5: Parameter updates
def update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate):
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    return W1, b1, W2, b2

# Step 6: Train the model
def train(X, Y, hidden_size, learning_rate, epochs):
    input_size = X.shape[1]
    output_size = Y.shape[1]
    W1, b1, W2, b2 = initialize_parameters(input_size, hidden_size, output_size)
    for epoch in range(epochs):
        # Forward pass
        Z1, A1, Z2 = forward_propagation(X, W1, b1, W2, b2)
        loss = compute_loss(Z2, Y)
        # Backward pass
        dW1, db1, dW2, db2 = backward_propagation(X, Y, Z1, A1, Z2, W2)
        # Update parameters
        W1, b1, W2, b2 = update_parameters(W1, b1, W2, db2, dW2, dW2, db2, learning_rate)
        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {loss:.4f}")
    return W1, b1, W2, b2

# Step 7: Test the model
def predict(X, W1, b1, W2, b2):
    _, _, Z2 = forward_propagation(X, W1, b1, W2, b2)
    return Z2

# Train the model

# Training data (already normalized)
X_scaled = np.array([[0.625, 0.667], [0.75, 0.333], [1.0, 1.0]])
Y_scaled = np.array([[0.547], [0.609], [0.75]])

# Train
W1, b1, W2, b2 = train(X_scaled, Y_scaled, hidden_size=4, learning_rate=0.01, epochs=1000)

# Test with a random input 

random_input = np.array([[4, 3]]) / np.array([[8, 3]])  # Normalize
predicted_scaled = predict(random_input, W1, b1, W2, b2)
predicted = predicted_scaled * 320  # Scale back to original range
print("Predicted zone 2 power:", predicted)

