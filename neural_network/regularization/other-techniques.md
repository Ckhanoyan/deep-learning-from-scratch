# Data Augmentation 

Data augmentation is a technique that can expand the size of a training dataset by applying various transformations to the existing data, e.g., cropping or flipping cat or dog pictures without having to pay more to get more data. This helps the model generalize better by being exposed to a wider variety of examples and avoiding overfitting. What are common augmentation techniques for images?
* Flipping
* Rotation
* Cropping
* Scaling
* Color Jitter
* Noise addition

To do this, you can use TensorFlow by using libraries like ImageDataGenerator.

# Early Stopping 

It is another regularization technnique that is used to halt the training process when the model's performance on a validation set stops improving. This will prevent overfitting by ensuring the model does not over-optimize on the training data. How it works:
* Monitor a performance metric, and if the metric stops improving for a predefined number of epochs, stop training.

To do this, you can use TensorFlow to support early stopping.

    from tensorflow.keras.callbacks import EarlyStopping 
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

Here's the code example I just set up:
[other-techniques.py](https://github.com/Ckhanoyan/deep-learning-from-scratch/blob/main/scripts/regularization/other-techniques.py)
