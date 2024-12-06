# What is a logistic regression?

Logistic regression is a statistical model that predicts probabilities. It is commonly used for binary classification problems, where the output is either 0 or 1. 

We compute the weighted sum of inputs and a bias like this below:
z = w.T * X + b

Then we apply the sigmoid function to z:
A = 1 / (1 + np.exp(-z))

**Real World Example: Email Spam Classification** 

What if you want to design a system to automatically classify emails as either "spam" (1) or "not spam" (0)? How will we determine what the X is? 

1. Consider input features, including numerical representations of email characteristics
** Number of links in the email
** Presence of specific keywords, e.g., "win", "free". etc. 
** Email length 
** Percentage of capitalized words 
** Number of typos 

2. Look at output labels 
** You want the output to be 1 for spam email and 0 for non spam email

3. Logistic regression steps: 

Weighted sum... calculate z = w.T + b
  w is the weight assigned to each email feature 
  b is the bias term 

Prediction (probability) is the ability to apply the sigmoid function to z, resulting in a probability Y^ between 0 and 1 

Decision: if Y^ > 0.5, then it will be rounded up to 1 and classify the email as spam. Otherwise, it will classify as 0 and not spam. 

4. Code example: 

import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Example data
w = np.array([0.5, 1.0, -0.5])
X = np.array([1.0, 0.0, 1.0])
b = 0.2

z = np.dot(w, X) + b
A = sigmoid(z)
print("Probability:", A)
