# Reshape an image

Why reshape? 

Deep learning frameworks expect inputs to be in a batch-first format, meaning the shape should be (number of samples, number of features). For example, use our house price practice: 

X (features) should be reshaped to [(3, 2, 1.5)] with shape (1, 3), representing one sample with three features. It means that it is good to go without needing to reshape it. 

W (weights) should remain as is, but in some cases, it might also need reshaping to (3, 1) for matrix multiplication if required. 

### Reshape the House Price Code: 

X = np.array([3, 2, 1.5]).reshape(1, -1)

W = np.array([25000, 10000, 200000)].reshape(-1, 1)

B = 100000

price = np.dot(X, W) + B

print("Predicted house price: ", price[0, 0])

### Key Points 

X is reshaped to (1, 3) to represent a batch of one sample with three features (bedrooms, bathrooms, and sq ft). 

W is reshaped to (3, 1) to represent the weights for three features, aligning with matrix multiplication rules. 

The output price is now a 2D array so we use price[0, 0] to access the scalar value.
