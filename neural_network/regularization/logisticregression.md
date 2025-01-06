# Logistic Regression

Logistic regression is a type of model that is used to predict outcomes such as "yes" or "no". It uses some math with weights W and bias b. How do we use it to prevent overfitting in a model?

<img width="700" alt="{783F55E3-8575-41DB-9A08-E2D5240B0E8D}" src="https://github.com/user-attachments/assets/533f6beb-909a-4bfd-9dbd-a976ccc25c0f" />

### The Equation for Logistic Regression 

The goal is to minimize a cost function like J(w, b) - see the photo I wrote. Look at it as the "error" for how wrong predictions may be. The smaller number, the better. 

### Regularization 

Regularization is like adding rules to make sure that the model does not overfit (in the other words, you do not want it to become too good at memorizing the training data but bad at new data like dev or test data). Presented by Andrew NG, there are two types of regularization for logistic regression such as below. 

* L2 Regularization: it adds a penalty based on the squares of the weights w, which encourages the weights to be small but does not make them exactly 0.
* L1 Regularization: it adds a penalty based on the absolute values of the weights w, which can make some weights zero and that means it can help the model focus on the important inputs.

### The Regularization Paramter
λ (lambda) is the regularization parameter that controls how much penalty to apply. 
* A larger λ makes the model simpler by applying more penalty.
* A smaller λ lets the model be more flexible but risks overfitting.

### Why Not Penalize b? 
The bias b is not penalized because it only has one parameter unlike the weights W. It also does not contribute to the complexity of the model in the same way as w. If you want to do it yourself, which is fine, it would not make a big difference. 
