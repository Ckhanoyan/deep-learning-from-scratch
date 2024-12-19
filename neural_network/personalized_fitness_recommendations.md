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
* Weight: user's weight in pounds (normalized)
* Availability: number of hours per week the user can dedicate to fitness (normalized)
* Fitness level: current fitness level encoded as 1) Beginner, 2) Intermediate, 3) Advanced
* Goal: fitness goal encoded as 1) weight loss, 2) muscle gain, 3) endurance improvement

### Example Input Matrix X

| Age  | Weight  | Availability | Fitness Level | Goal |
|------|---------|--------------|---------------|------|
| 0.25 | 0.60    | 0.50         | 1             | 1    |
| 0.40 | 0.80    | 0.75         | 2             | 2    |
| 0.35 | 0.70    | 0.30         | 3             | 3    |
