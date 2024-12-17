For X,
* Hours of sleep
* Hours of riding a bike

For Y,

Average zone 2 power

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

Normalize X

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

Normalize Y

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

I hope this example above helps you and also myself understand how to normalize both X and Y in simple step by step.
