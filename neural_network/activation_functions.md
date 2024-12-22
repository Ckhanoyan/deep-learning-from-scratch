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

### ReLU (Rectified Linear Unit) activation function 
* ReLU activiation function, a = max(0, z), where it introduces non-linearity and avoids the vanishing gradient problem by having gradients of either 0 or 1 for positive inputs.
* Use case: most commonly used in hidden layers of deep neural networks due to its computional efficiency and effectiveness in training.. However, it can lead to "dead neurons" if many outputs are zero or negative. 
* Real world example: It seems more popular in modern neural networks... It can be used in healthcare where it can predict disease diagnoses from medical images, e.g., identifying tumors in X-rays or MRIs. For gaming, it can be used to train AI agents in video games to make real-time decisions like reinforcement learning in chess games, and it supports deep neural networks by enabling faster training, etc.

<img width="500" alt="{FD875301-4E36-4E29-AF89-06A274934087}" src="https://github.com/user-attachments/assets/64987436-a37e-4a16-b7b5-8b3bb817fa4b" />

### Leaky ReLU activation function
* Leaky ReLU activation function, a = max(0.01z, z), where it addresses the "dead" neuron issue in standard ReLU by allowing a small, non-zero gradient for negative inputs.
* Use case: used in deep neural networks where ReLU fails due to dead neurons
* Real world example: again, we are talking about healthcare, it can be used to analyze medical data to detect conditions such as diabetes, heart disease, or cancer. Why? Medical datasets may contain features with negative values such as deviations in lab results. Leaky ReLU can ensure that all data can contribute to the model. Also, for weather forecasting, weather data can have negative values such as temperature dropping below zero.

<img width="500" alt="{F8F034AC-EB1E-4C81-9DDD-132414BE3A12}" src="https://github.com/user-attachments/assets/05cde939-c116-4c6f-b704-f1c004069e03" />
