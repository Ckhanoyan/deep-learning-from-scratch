# Calculate the Gradient for the Sigmoid Function Using Health Insurance Approval Prediction 

We would use it during backpropagation for logistic regression. Remember the sigmoid function below: 

    σ(x)= 1 / (1 + np/exp(-x))
​
Here is the gradient of sigmoid function, which this formula leverages the property of the sigmoid function to simplify computation. 

    σ'(x) = σ(x) ⋅ (1−σ(x))

Compute the gradient for each input so if we want to find Ypred (Y prediction) coming from (z = Xw + b, the weighted input: 

    σ′(z) = Ypred * (1 - Ypred) 
