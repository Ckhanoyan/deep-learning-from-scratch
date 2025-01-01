# Forward Propagation in Deep Neural Network

<img width="600" alt="{36D93ED1-C957-461A-B679-A33D70C4E81C}" src="https://github.com/user-attachments/assets/85bc171d-8409-47eb-8550-c09601bd6788" />

Structure of the neural network above:
* input layer: X = [x1, x2, x3]
* 3 hidden layers and one output layer making it 4 total layers (x layer is layer 0)

## Forward Propagation 

### Layer 1 (input to Hidden Layer 1) 
Compute the pre-activation by doing z[1] = w[1] X + b[1] and then you apply the activation function such as sigmoid, tanh, or ReLU by doing a[1] = g(z[1]) 

### Layer 2 (hidden layer 1 to hidden layer 2) 
Compute the pre-activation by doing z[2] = (w[2],a[1]) + b[2] and then you apply the activation function by doing a[2] = g(z[2]) 

### Layer 3 and it goes on until the final output (see the photo) 

## Vectorized computation 

Remember that we would like to do execuation at once instead doing a loop for each function or whatever we have. This process has matrix multiplications for weights and activations, which will work effectively in either PyTorch or TensorFlow.
