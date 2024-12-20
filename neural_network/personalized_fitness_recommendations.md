# Real Life Use Case: Personalized Fitness Recommendation System

This is my practice to understand the vectorization process for multiple examples so I am trying to build a personalized fitness model that would then recommend workouts based on an user's profile that contains age, weight, fitness level, goal, and availability for training.  

Let's say that our system will predict the optimal type of workout, e.g., 1) cardio, 2) strength training, 3) HIIT, etc., and also intensity level for each person. 

What we know is that each user's profile is considered as a feature vector x(i) containing both numerical and categorizal data. With using machine learning and vectorization, inputs will be passed through a model with weights and biases and process hundreds or thousands of users with prediction all at once, which is my goal. 

## Input Matrix X for Personalized Recommendations

### Structure of Matrix X:
- **Rows:** Represent individual users
- **Columns:** Represent key features, e.g. age, weight, etc. 
- **Values:** Numerical or categorical data normalized or encoded 

### Features Included in X Example:

* Age: age of the user (normalized between 0 and 1)
* Weight: user's weight in kg (normalized)
* Availability: number of hours per week the user can dedicate to fitness (normalized)
* Fitness level: current fitness level encoded as 1) Beginner, 2) Intermediate, 3) Advanced
* Goal: fitness goal encoded as 1) weight loss, 2) muscle gain, 3) endurance improvement

### Example Input Matrix X

| Age  | Weight  | Availability | Fitness Level | Goal |
|------|---------|--------------|---------------|------|
| 0.25 | 0.60    | 0.50         | 1             | 1    |
| 0.40 | 0.80    | 0.75         | 2             | 2    |
| 0.35 | 0.70    | 0.30         | 3             | 3    |

### Explanation 

User 1 is 25 years old (25% of the normalized range of 0-100, weighs 60% (or 60 kg) of the normalized range of 0-100 kg, can dedicate 50% of the max hours (e.g., 5 hours if the max is 10), is a beginner for his fitness level. For his goal, it is weight loss. The same goes to the other users in the table. 

### Matrix X in Python Using Numpy

    import numpy as np

    # Example Input Matrix X
    X = np.array([
      [0.25, 0.60, 0.50, 1, 1],  # User 1
      [0.40, 0.80, 0.75, 2, 2],  # User 2
      [0.35, 0.70, 0.30, 3, 3]   # User 3
    ])

    # Print the matrix
    print("Input Matrix X:")
    print(X)

Above is the 3 x 5 matrix. Thus, the formula - X ∈R n x m - represents a matrix X that belongs to the space of real numbers (R) and has dimensions of n x m, where: 
* n is the number of rows, e.g., the number of users
* m is the number of columns, e.g., features, attributes, etc.

For this recommendation system here, the formula defines a dataset where each row corresponds to an user, and each column corresponds to a specific feature.

### Define output labels for this system 

We want to have the output defined, and I probably should call it the "recommended workout type", which is categorical. Here are the five categories I can think of, and we may need to one-hot encode these labels into Y. One-hot encoding is a method to represent cateogrical data in a binary format, which means that each cagtegory is transformed into a vector of zeros with a single 1 indicating the presence of that category. 
* Cardio
* Strength training
* HIIT
* Yoga
* Flexibility

This is an example of transforming the categorical variables into binary variables: 

        [1, 0, 0, 0, 0] #cardio
        [0, 1, 0, 0, 0] #strength training 
        [0, 0, 1, 0, 0] #HIIT
        [0, 0, 0, 1, 0] #yoga 
        [0, 0, 0, 0, 1] #flexibility 

This is how you one-hot encode the labels into Y, where Y ∈R ↑ (5 x m) for 5 workout types.

### Implement Forward Propagation 

The forward pass will compute predictions for all users using vectorization. Here's the linear combination:

Z = np.dot(W, X) + b 
* Where W is the weight matrix
* Where b is the bias term

The next step will be utilize softmax activiation (A = softmax(Z)) that will then convert raw scores into probabilities that sum to 1. 

[data_preprocessing_workout.py](https://github.com/Ckhanoyan/deep-learning-from-scratch/blob/main/scripts/data_preprocessing_workout.py)
