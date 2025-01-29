# Tuning Hyperparameters 

After learning core techniques on how to implement a neural network, understanding which hyperparameters to prioritize is critical for effective model training. Based on my learning process, it is clear that the learning rate is the most important hyperparameter to consider before other hyperparameters. The learning rate can control how quickly the model can adjust its weights during training so the best practice is to try a few different values on a logarithmic scale from 0.1 to 0.001. 

### The Learning Rate and What Else?

Once the learning rate is set, the batch size is the next thing we should consider fine-tuning. Smaller batch sizes can offer more frequent updates and better computation/generalization. However, they can introduce more noise into the process. What about larger batch sizes? Surely, they can reduce the noise and be more stable but can cause slower updates and lead to poorer generalization. This depends on computational resources we have. 

### Okay. The Learning Rate, Batch Size, and What Else? 

Another hyperparameter to consider is the number of layers and hidden units per layer in a neural network! Increasing the number of layers and/or units can lead to overfitting so it is important to balance model complexity with the risk of overfitting by using regularization techniques like dropout and/or cross-validation. Note that there is a file in this repository explaining more about the regularization techniques. 
