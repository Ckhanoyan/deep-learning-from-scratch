# Face Recognition 

## One-Shot Learning 

This approach in deep learning refers to the ability of a model to learn from one or a few examples of each class such as an individual (unlike a traditional approach using a large dataset for training). One shot learning approach is useful in face recognition where we can just need the model to recognize individuals based on even one image (a few is better) per person. Often times, we may need to do the Siamese Network approach for this. 

## Siamese Network 

Siamese Network contains two identical neural networks such as CNNs in face recognition, and the approach also uses the same weights and parameters for this purpose. The two networks then uses two different images such as Chris (myself) and my son, and they will be then computed featuring embeddings for each of the images. The purpose of this is to learn a metic that can be either a difference/distance or similarity between the images. That may be interesting since my son and I look alike! We need to consider some step by step work below:

* Dual inputs: the approach takes two inputs (two images)
* Feature extraction: Both the images are being processed through the same CNNs (same weights and same parameters) to extract feature vectors that represent key characteristics of our faces (let's see about that).
* Distance metric: after extracting the feature vectors, they are then compared using a distance metric that gives a measure of how either different or similar our two faces are to each other. Given the equation, the distance should be small if there is the same person from both the images. The distance should be large if my son and I are different individuals in the images.
* Output layer: The network's output layer comes with a binary classification...
* Loss function: it is often used in this network.

This is a great resource to learn: https://medium.com/@rinkinag24/a-comprehensive-guide-to-siamese-neural-networks-3358658c0513
