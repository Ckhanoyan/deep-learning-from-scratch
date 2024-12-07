import numpy as np

# Features for one sample (reshaped for batch processing)
X = np.array([3, 2, 1.5]).reshape(1, -1)

# Weights
W = np.array([25000, 10000, 200000]).reshape(-1, 1)

# Bias
B = 100000

# Predicted price using matrix multiplication
price = np.dot(X, W) + B

print("Predicted house price: ", price[0, 0])
