# Mini-Batch Gradient Descent 

MBGD is a variation of the standard gradient descent optimization algorithm used in machine learning and deep learning. It strikes a balance between two other forms of gradient descent.This MBGD seeks to combine the benefits of the other forms, and it updates the model parameters based on a small, random subset of the training data rather than using one example or the entire dataset. The purpose of doing this is to speed up computation or that it would be very slow if you had a large dataset. 

### How It Works 

You can split the dataset into smaller mini-batches, and each mini-batch can contain a number of training examples such as 100, 200, or 400 samples. Therefore, for each mini-batch, the gradient of the loss function is computed with respect to the model parameters. The process is then repeated for each mini-batch until all mini-batches have been processed. One complete pass over the entire dataset is called an epoch. 

### What About Other Forms? 

* Stochastic Gradient Descent is a form that updates the model parameters using only one training example at a time. While this makes SGD fast, it is highly noisy and can lead to unstable updates, making it difficult to converge to the optimal solution.

* Batch Gradient Descent computes the gradient based on the entire dataset, which provides stable and updates but can be computationally expensive and inefficient, especially for large datasets.

### Plots 

**Batch Gradient Descent**
  
![image](https://github.com/user-attachments/assets/33a5b40f-354e-4df3-9883-10e6a400f504)

This image comes from https://www.bogotobogo.com/python/scikit-learn/scikit-learn_batch-gradient-descent-versus-stochastic-gradient-descent.php

Description: this takes the average of the gradients of all the training examples and then uses the mean gradient to update the parameters.

**Stochastic Gradient Descent**
  
![image](https://github.com/user-attachments/assets/f7817b48-6dda-4369-8a84-160a0f184c10)

This image comes from https://adventuresinmachinelearning.com/stochastic-gradient-descent/

Description: this approach is better for a large dataset. The more the data the more chances of a model to be good or better. If it has over 5 million samples, it does not make sense to use Batch Gradient Descent as it would be ineffective. Stoachastic Gradient Descent consideres one example at a time to take a single step, which means 1) taking an example, 2) feeding it to the neural network, 3) calculating its gradient, 4) using the gradient calculated in step 3 to update the weights, and 5) repeating steps 1-4 for all the examples in training dataset. It will keep dancing for a long time until it almost reaches the minima. 

**Mini-batch Gradient Descent**

![image](https://github.com/user-attachments/assets/fe75fa53-ec8e-4ea7-b9ec-7d202c342e6e)

This image comes from Andrew NG's deep learning courses (Coursea). 

Description: this mini-batch gradient descent is ideal for updating parameters frequently, including for vectorized implementation for faster computations. 
