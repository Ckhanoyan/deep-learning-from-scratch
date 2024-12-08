# What is np.random.seed? 

A random seed is a number that initializes a random number generator. While the generated numbers are still pesudo-random, using the same seed ensures that the sequence of random numbers is reproducible.

Without a seed, the random numbers would be different each time you run the code. In the other words, you can generate the same "random" results for any reasons. 

What happens without using a seed? The random numbers will differ. 

## Simple example using a house pricing model
We want to set the seed for reproducibility so we can just set up np.random.seed(42)

We will generate random data for the number of bedrooms, bathrooms, and square footage such as below:

### Set the seed for reproducibility 
np.random.seed(42)

### Generate random data for the number of bedrooms, bathrooms, and sq. footage
num_houses = 100 

### (Number of bedrooms [1 to 5])
num_bedrooms = np.random.randint(1, 6, size=num_houses)


### (Number of bathrooms [1 to 3])
num_bathrooms = np.random.randint(1, 4, size=num_houses)

### (Square footage between 500 and 3000 sq. feet)
square_footage = np.random.randint(500, 3000, size=num_houses)

