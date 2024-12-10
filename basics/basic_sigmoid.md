# Basic Sigmoid in Deep Learning 

The sigmoid function is a mathematical function often used in deep learning (activation of neurons) so it maps real-valued input to a range between 0 and 1 to determine probabilities or binary decisions.

Formula looks like below: 

    σ(x)= 1 / (1 + np.exp(-x))

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

### Simple Example in Python for Health Insurance Approval Prediction 

This code includes some synthetic data using NumPy as a basic example (based on my learning...) 

    import numpy as np
    import matplotlib.pyplot as plt
    
    # Define the sigmoid function
    def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
    # Sample input data representing applicant features
    # Let's assume:
    # - Age
    # - BMI (Body Mass Index)
    # - Smoking status (0 = non-smoker, 1 = smoker)
    
    # Let's create some sample applicants
    # [Age, BMI, Smoking Status]
    applicants = np.array([
        [25, 22, 0],  # Young, healthy, non-smoker
        [40, 28, 0],  # Middle-aged, average BMI, non-smoker
        [30, 30, 1],  # Young, overweight, smoker
        [55, 32, 1],  # Older, high BMI, smoker
        [22, 20, 0],  # Very young, low BMI, non-smoker
    ])
    
    # Define weights for the model (simplified)
    # These would usually be determined during training in a real-world model
    weights = np.array([0.05, 0.03, -0.5])  # Small positive weights
    
    # Calculate a simple dot product (linear combination of features and weights)
    logits = np.dot(applicants, weights)
    
    # Apply the sigmoid function to get approval probabilities
    approval_prob = sigmoid(logits)
    
    # Print the approval probabilities
    print("Approval probabilities:", approval_prob)
    
    # Plot probabilities
    plt.bar(range(len(approval_prob)), approval_prob, color="skyblue")
    plt.title("Health Insurance Approval Probabilities")
    plt.xlabel("Applicant")
    plt.ylabel("Probability of Approval")
    plt.show()

How did we determine these weights? In this demonstration, arbitrary weights were selected to simulate a simple relationship:
* These weights represent the influence of each feature on approval decisions.
* Small positive weights (0.05 and 0.03) simulate positive influences on approval.
* The negative weight (-0.5) for smoking suggests that smoking negatively impacts insurance approval, as smokers are often considered higher-risk applicants.

What is the purpose of logits = np.dot(applicants, weights)?
* This line is calcualating the weighted sum of input features.
* Each row of an applicant has 3 values (age, BMI, smoking status) like Column 0, Column 1, Column 2
* Weights is a 1-dimensional array representing the importance of each input feature
* What does np.dot do??? The dot product of two matrices multiplies each row in applicants with the weights array element-wise and sums up the results of each 


![image](https://github.com/user-attachments/assets/177edda5-9ec0-47e9-86d5-5385cd9601f5)


![image](https://github.com/user-attachments/assets/8e238f72-b978-44ae-8729-4736fe741955)


