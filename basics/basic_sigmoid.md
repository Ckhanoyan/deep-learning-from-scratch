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
