# Basic Sigmoid in Deep Learning 

The sigmoid function is a mathematical function often used in deep learning (activation of neurons) so it maps real-valued input to a range between 0 and 1 to determine probabilities or binary decisions.

Formula looks like below: 

    σ(x)= 1 / (1 + e−x1)

Where e is the base of the natural logarithm (= 2.718), and x is the input value (any numbers).
​

![image](https://github.com/user-attachments/assets/c52d661a-f88b-41fe-a425-7392771f5b53)


Plot explanation: 
  The curve smoothly transitions from 0 to 1. At X = 0, the output is 0.5. It has the "S" shape, which is why it is called "sigmoid". 
  The key characteristics you see in the plot are 1) outputs close to 0 represent a prediction of the negative class and 2) outputs close to 1 represent a prediction of the positive class. 

## Real World Use Case: Health Insurance Approval Prediction 

Health insurance companies often use machine learning models to decide whether to approve or reject an applicant's request for coverage. Input features typically include age, weight, smoking status, medical history, family health history, and phsyical activity. 

For model training, a logistic regression model will use these input features to analyze an applicant's risk profile. The sigmoid function output will be between 0 and 1. 

An output of 0.8 means an 80% probability of approving the insurance application. 

An output of 3.0 means a 30% probability of approving it. 

The decision threshold, e.g., 0.5, is set. so if probability > 0.5, approve the application. If probability < .5, reject the application. 
