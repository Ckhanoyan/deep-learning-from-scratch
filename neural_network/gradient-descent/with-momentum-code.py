import numpy as np
import matplotlib.pyplot as plt

def compute_cost(theta):
    return theta ** 2

def compute_gradient(theta):
    return 2 * theta

def gradient_descent_with_momentum(start_theta, learning_rate, beta, num_iterations):
    theta = start_theta
    v = 0  # Initialize velocity
    cost_history = []

    for i in range(num_iterations):
        grad = compute_gradient(theta)
        v = beta * v + (1 - beta) * grad  # Update velocity
        theta = theta - learning_rate * v  # Update parameters
        cost = compute_cost(theta)
        cost_history.append(cost)
        print(f"Iteration {i+1}: theta = {theta}, cost = {cost}")

    return theta, cost_history

# Parameters
start_theta = 4
learning_rate = 0.1
beta = 0.9  # Momentum factor
num_iterations = 50

# Run gradient descent with momentum
optimal_theta, cost_history = gradient_descent_with_momentum(start_theta, learning_rate, beta, num_iterations)

# Plot the cost function over iterations
plt.plot(cost_history)
plt.title('Cost Function Over Time (Gradient Descent with Momentum)')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()

print(f"Optimal theta: {optimal_theta}")
