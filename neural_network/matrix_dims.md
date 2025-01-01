# How to get your matrix dimensions right 

<img width="600" alt="{D50FB7DE-762E-490B-B898-3C286B2B0834}" src="https://github.com/user-attachments/assets/4aed0ad0-7008-43fb-ac69-dd719a25bc40" />

I made this drawing to document my learning process on how to get matrix dimensions right and understand why it is important to make sure that the numbers are correct in coding or documentation. Here are the key components to consider: 

### Neural network architecture 
This network has layers indexed [0], [1]. [2], [3], [4], and [5]. The [0] is the input layer. 1-4 are the hidden layers. The [5] layer is the output. So, each layer has a number of neurons such as that the [1] layer has three neurons, the [2] layer has five neurons, and it goes on. 

### Forward Propagation Formula 
I do not need to explain the whole formula again, but remember that we have to compute the pre-activation and then activation function for each layer. Z[l] is the pre-activation output, W[l] is the weight matrix, A[l-1] is the activation from the previous layer, b[l] is the bias vector, and g(*) is the activation function. 

### Why Matrix Dimensions Matter 
We have to ensure correctness for all matrix multiplications or that the computation will not proceed or not proceed effectively. I think with this drawing I made and I learned from Andrew NG in deep learning courses, this really helps me understand the neural network architecture so that way I can ensure proper matrix dimensions in case if I ever come across coding or problem solving. 
