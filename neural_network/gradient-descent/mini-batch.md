# Mini-Batch Gradient Descent 

MBGD is a variation of the standard gradient descent optimization algorithm used in machine learning and deep learning. It strikes a balance between two other forms of gradient descent.This MBGD seeks to combine the benefits of the other forms, and it updates the model parameters based on a small, random subset of the training data rather than using one example or the entire dataset. The purpose of doing this is to speed up computation or that it would be very slow if you had a large dataset. 

### How It Works 

You can split the dataset into smaller mini-batches, and each mini-batch can contain a number of training examples such as 100, 200, or 400 samples. Therefore, for each mini-batch, the gradient of the loss function is computed with respect to the model parameters. The process is then repeated for each mini-batch until all mini-batches have been processed. One complete pass over the entire dataset is called an epoch. 
