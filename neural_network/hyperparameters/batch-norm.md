# Batch Norm

Yes, this is another technique we need to know. Think of this real life analogy below:

## Metaphor: Making a Team Work Better Together
Imagine you're managing a sports team (say, a soccer team). The team members are all players with different levels of skill and experience, and you want them to perform as efficiently as possible during a game.

Now, think of the team players as the neurons in a neural network. Each player (neuron) has their own strengths (activations) based on how well they can play (how much their output contributes to the next layer in the network).

**But here's the issue**:

Some players may overperform (too much energy, too fast), making the team unstable.
Some players may underperform (not enough energy), and that slows down the team's ability to move the ball or score goals.
What do you do to fix it?

You normalize the performance of the players so that they’re all contributing at the same pace:

You standardize their effort so they all have the same energy output.
You make sure everyone is playing at the optimal level (not too little, not too much).
You adjust the strategy to make sure that each player is performing just right (optimizing their activations), so the whole team works better together, and the game flows smoothly.

In the world of neural networks, normalizing activations ensures that every "player" (neuron) in the network is contributing appropriately, leading to faster learning and a more stable model.

## Equations USed in Batch Norm (BatchNorm)

Batch normalization is applied to the activations of a layer in a neural network, which normalizes the activations by ensuring that the output has a mean of 0 and a standard deviation of 1 for each feature in a batch. We have to compute the mean and variance for each feature over the mini-batch. So, for a mini-batch B with m samples, each having d features where x(i) represents the activation of the i-th sample in the mini batch), you compute both the mean and variance.

Mean: 

<img width="400" alt="{70806F99-025C-41CB-86D6-1ADA82531D55}" src="https://github.com/user-attachments/assets/e434a197-3e73-4c03-b165-cb25dcefa65d" />

Where μB is the mean activation for the entire batch over the features. 
​

Variance:

<img width="400" alt="{2AF40B42-B74E-49F4-A9C7-A52EBC949FE1}" src="https://github.com/user-attachments/assets/bce54065-0493-4fe5-be4b-c24a51992c42" />

Where σB2 is the variance of the activations for each feature across the mini-batch.


Once the mean and variance are computed, the activations are normalized by subtracting the mean and dividing by the standard deviation (which is the sq root (sqrt) of the variance):

<img width="350" alt="{13EE1FC9-FB3C-47D6-BB69-F1B908547D89}" src="https://github.com/user-attachments/assets/09869c5e-9778-4653-a6da-c493025b53ed" />

Where x^(i) is the normalized activation for the i-th sample. Also, epilson is a small number added for numerical stability.


Finally, we can scale and shift (learnable parameters)... After normalizing the activations, we want to scale and shift the normalized values, which will allow the network to retain the capacity to model complex distributions of activations. The learnable parameters (scale and shift - γ and β) then come into play as they are learned during training and allow the network to undo the normalization if necessary, giving it some flexibility. 

<img width="400" alt="{D0D7C72D-84E7-44DF-9D81-681D706FE9B1}" src="https://github.com/user-attachments/assets/4bd40b7e-b394-41c5-b2a0-309444ccc53d" />

γ is the scale parameter (a vector of learnable parameters, one for each feature).
β is the shift parameter (a vector of learnable parameters, one for each feature).
𝑦(𝑖) is the final output after the normalization, scaling, and shifting.

## So... What is our conclusion???

So, in simple terms, Batch Normalization is like giving your neural network a well-needed coffee break during training. By standardizing those activations, it ensures the network doesn’t go off the rails with wild fluctuations, like a person on an energy rush or a burnout. Then, with the scaling and shifting, it's like giving the network a fancy espresso shot—just enough to wake it up and help it make the right decisions for faster, smoother training.

In short, BatchNorm keeps your network chill, focused, and ready to get to work—without breaking a sweat.
 
 
