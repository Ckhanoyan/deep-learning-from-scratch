# Calculate the Gradient for the Sigmoid Function Using Health Insurance Approval Prediction 

We would use it during backpropagation for logistic regression. Remember the sigmoid function below: 

    σ(x)= 1 / (1 + np/exp(-x))
​
Here is the gradient of sigmoid function, which this formula leverages the property of the sigmoid function to simplify computation. 

    σ'(x) = σ(x) ⋅ (1−σ(x))

Compute the gradient for each input so if we want to find Ypred (Y prediction) coming from (z = Xw + b, the weighted input: 

    σ′(z) = y_pred * (1 - y_pred) 

If we are calculating gradients for logistic regression, we should calculate the gradient of the loss function as well. 

    Loss = -(1/N) * Σ [y_i * log(y_pred) + (1 - y_i) * log(1 - y_pred)]

With above, you will find Error from this formula:

    error = y_pred - y_true

