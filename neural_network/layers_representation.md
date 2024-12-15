# Neural Network Representation

Think of a simple diagram representing a neural network using nodes and connections (1 input layer and 1 hidden layer and 1 output layer). We may have 3 features (input), 4 nodes within the hidden layer, and 1 node in the output layer. 
* Input layer: 3 input features such as x1, x2, x3, etc.
* Hidden layer: 4 nodes such as h1, h2, h3, h4
* Output layer: 1 node representing the final prediction y 

![image](https://github.com/user-attachments/assets/d2b3fc9c-afbb-46b6-9dee-0e7eb9906f1e)

Please understand that the hidden layer only has ONE single layer made of 4 neurons, e.g., w = [4,3] and b = [4,1]. However, networks can have multiple hidden layers, and this is just an example with one hidden layer that helps me learn easier. 

I am using one example as my learning process from this link below but also replace the numbers with my own random numbers and a different scenario:

https://becominghuman.ai/understanding-the-structure-of-neural-networks-1fa5bd17fef0

For X,
* Hours of sleep
* Hours of riding a bike

For Y, 
* Average zone 2 power

      X = np.array(([5,2], [6,1], [8,3]), dtype=float)
      Y = np.array(([175], [195], [240]), dtype=float)

For X output, we get this below:

      [[5.  2. ]
       [6.  1. ]
       [8.  3. ]]

For Y output, we get this below:

      [[175.]
       [195.]
       [240.]]

However, since both X and Y are not normalized yet as they need to be. We have to scale them to between 0 and 1 for the max value purpose. What do we expect from this new model? 
* Input layer: Two features (hours of sleeping and hours of riding)
* Hidden layer: small layer with a new neurons that learn latterns in the data
* Output layer: produces one output such as the predicted average zone 2 power

### Normalize X

X = X / Xmax, where X max is a vector of the max values for each column of X. Example below: 

      [[5  2 ]
       [6  1 ]
       [8  3 ]]

       X max = [8 3]

Then we can divide the first one by the X max such as this below: 

       X scaled = 
      [[5  2]
       [6  1]
       [8  3]]
       / 
       [8  3]

We get the X normalized output below:

      [0.625  0.667]
      [0.75   0.333]
      [1      1]

Then, we do the same thing for Y, and the max Y value is 320. 

      [175]
      [195]
      [240]
      /
      [320]

Y output:

      [0.547]
      [0.609]
      [0.75]


