# Activation Functions 

I did not realize there were some activation functions we could choose based on our use cases or values. I learned that the choice of activation functions is critical in neural networks where they will determine how the model learns and represents complex relationships in the data. We have some types of activation functions such as below:

### Sigmoid activation function
* Sigmoid activation function, a = 1 / (1 + e (-z)), where it maps input values to a range between 0 and 1 (binary) so it can be used for probabilities.
* Use case: commonly used in the output layer for binary classification problems like it will tell you if an email is spam or not. 

<img width="500" alt="{823C34CF-572D-4924-9698-14203D7677E6}" src="https://github.com/user-attachments/assets/c7dde871-1bfa-4c09-933f-f8404df125f3" />

### Tanh activation function
* Tanh activation function, a = (e(z) - e(-z)) / (e(z) + e(-z)), where it maps input values to a range between -1 and 1, centering the output. It often performs better than sigmoid for hidden layers because the mean of its outputs is closer to zero.
* Use Case: frequently used in hidden yaers of neural networks, RNNs, where centering around zero helps in reducing training time.
* Real world example: better when data has both positive and negative values. For example, we can use it for sentiment analysis where it determines positive, negative, or neutral reviews or social media posts. Sentiment scores often range from highly negative to highly positive, and the tanh formula (-1 to 1) aligns well with this data, 

<img width="500" alt="{3A4E0F7B-FC33-4E19-AF24-BD5ECF3455FF}" src="https://github.com/user-attachments/assets/22b9677d-1977-4c56-93f4-f5ec5962d966" />

