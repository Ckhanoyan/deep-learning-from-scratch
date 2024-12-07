# Numpy.array

numpy.array is a versatile tool for creating multi-dimensional arrays, which serve as the backbone for numerical operations in deep learning. These arrays enable efficient storage and manipulation of large datasets, matrix operations, and mathematical computations, making them essential for handling tensors, the primary data structures in deep learning frameworks like TensorFlow and PyTorch.

## Example with numpy.array

In deep learning, you often work with image data represented as tensors. For example, a color image with dimensions 
64
×
64
64×64 (height x width) and 3 color channels (RGB) can be stored as a 3D NumPy array:

import numpy as np

image = np.random.randint(0, 256, size=(64, 64, 3), dtype=np.uint8)

print("Image shape:", image.shape)

## Real World Use Case with numpy.array

What if you're training a neural network to predict housing prices based on three features: number of bedrooms, numbers of bathrooms, and size of the house (in square feet)?

Data you have below:

1. Input features (X):

    Bedrooms (1) 

    Bathrooms(2)

    Size (1000 sq ft) 

2. Weights (W):

    Price contribution per bedroom: 25,000
  
    Price contribution per bathroom: 10,000
  
    Price contribution per 1000 sq ft: 200,000

3. Bias (B):

   Base price: 100,000

Using these above, you predict the price as 

Y = W * X + B

### Example

For a house you like with 3 bedrooms, 2 bathrooms, and 1500 sq ft in Washington, Seattle, compute the price: 

Step 1) import numpy as np

Step 2) Features: [Bedrooms, Bathrooms, Size (in 1000 sq ft)]

X = np.array([3, 2, 1.5])

Step 3) Weights: [Price per bedroom, Price per bathroom, Price per 1000 sq ft]

W = np.array([25000, 10000, 200000])

Step 4) Bias: Base Price 

B = 100000
