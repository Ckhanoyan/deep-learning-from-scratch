import numpy as np

X = np.array([3, 2, 1.5])

W = np.array([25000, 10000, 200000])

B = 100000

price = np.dot(W, X) + B

print("Predicted house price: ", price)
