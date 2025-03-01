import numpy as np

# example data 
X = np.random.rand(3, 5) # 3 features, 5 examples 

# Layer 1: Weights and Biases
W1 = np.random.rand(4, 3) # 4 neurons, 3 features 
b1 = np.random.rand(4, 1) # biases for 4 neurons 

# Layer 1 computations 
Z1 = np.dot(W1, X) + b1 # weighted sum 
A1 = 1 / (1 + np.exp(-Z1)) # sigmoid activation 

# Layer 2: Weights and Biases
W2 = np.random.rand(2, 4)  # 2 neurons, 4 inputs from layer 1
b2 = np.random.rand(2, 1)  # Biases for 2 neurons

# Layer 2 computations
Z2 = np.dot(W2, A1) + b2 # weighted sum
A2 = 1 / (1 + np.exp(-Z2))  # Sigmoid activation

print("Output of the network: ")
print(A2)
