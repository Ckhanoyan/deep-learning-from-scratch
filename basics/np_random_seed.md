# What is np.random.seed? 

A random seed is a number that initializes a random number generator. While the generated numbers are still pesudo-random, using the same seed ensures that the sequence of random numbers is reproducible.

Without a seed, the random numbers would be different each time you run the code. In the other words, you can generate the same "random" results for any reasons. 

What happens without using a seed? The random numbers will differ. 

## Simple example using a house pricing model
We want to set the seed for reproducibility so we can just set up np.random.seed(42)

We will generate random data for the number of bedrooms, bathrooms, and square footage such as below:

### 1. Set the seed for reproducibility 
np.random.seed(42)

### 2. Generate random data for the number of bedrooms, bathrooms, and sq. footage
num_houses = 100 

### 3. (Number of bedrooms [1 to 5])
num_bedrooms = np.random.randint(1, 6, size=num_houses)

### 4. (Number of bathrooms [1 to 3])
num_bathrooms = np.random.randint(1, 4, size=num_houses)

### 5. (Square footage between 500 and 3000 sq. feet)
square_footage = np.random.randint(500, 3000, size=num_houses)

### 6. Calculate house prices based on the given formula
For example, we are doing this: Price = 100,000 + (# bedrooms * 50,000) + (# bathrooms * 30,000) + (square footage * 100). The code will look like something below:

house_prices = 100_000 + (num_bedrooms * 50000) + (num_bathrooms * 30000) + (square_footage * 100)

### 7. Visualize the data for square footage and house prices
plt.scatter(square_footage, house_prices, color='b', alpha=0.7)

plt.title('House Prices vs. Square Footage')

plt.xlabel('Square Footage')

plt.ylabel('House Prices')

plt.show()

### 8. Print some sample data

    for i in range(5):   
       print(f"House {i + 1}: Bedrooms: {num_bedrooms[i]}, Bathrooms: {num_bathrooms[i]}, Square Footage: {square_footage[i]}, Price: ${house_prices[i]}")




