# Normalizing Data 

What does "normalizing data" mean? Normalizing data in machine learning or deep learning is actually critical because it may improve the performance and stability of the model such as when using gradient-based optimization algorithms. For example, multiple features in real-world data have different scales like age from 0-100 and income from 0 to billions. Without normalizing data, this may affect the model. 

## Health Insurance Approval Prediction (Scenario)

Suppose that you try to predict whether or not you will be approved for your health insurance using the features. Features include below:
* Age (in years): 0 to 100
* Annual Income (in dollars): $0 to $500000
* Number of dependents: 0 to 10

How does normalization help with this information above? 

Suppose that you feed all of this RAW data into the machine learning model, what might happen is that the model may focus too much on annual income because its numbers are in the hundreds of thousands (that is when I now understand why normalization is necessary! Bingo.). 
