# Basic Recipe for Bias and Variance

So, this seems important to have this recipe to detect whether or not your model has either high bias or/and high variance. This also helps guide our approach to improving the model so that way we will have our targeted actions to adjust the model complexity such as using regularization, changing the algorithm, increasing the dataset size, and/or building a bigger network/model. 

Suppose that if we have high bias from training data performance, we may:
* build a bigger network/model
* train longer

Then it goes back to training data performance, and then it does not have high biases anymore. We may then check if it has high variance from dev set performance. If it does, then we may:
* add more data or increase the dataset size
* do regularization


