# How to normalize train sets and why 

This technique allows subtracting the mean and normalizing variance for a dataset in deep learning (as a way to prepare data). Based on my understanding from the course taught by Andrew NG:
* What "Subtract the Mean" means: we calculate the average value (mean) across the entire dataset and subtract this mean from every data point. For example, if we have student test scores [70, 80, 90], the mean is 80. Subtracting the mean will give us [-10, 0, 10].

# Normalize the variance 

What does normalizing the variance look like in deep learning? We calculate the standard deviation for each feature and then divide each data point by this value. That way we will make sure that all features have the same scale or level of variation. What does it mean given the student test scores?
* We will use centered scores [-10, 0, 10], and the standard deviation is sqrt(((-10)^2 + 0^2 + 10^2) / 3) = 10.
* Divide each value by 10 gives us: [-1, 0, 1].

# The Point and Use Case
The data will become standardized where will help the model learn faster and more effectively. Here's the example using house prices. There are features such as the size of the house, number of rooms, distance to the city center, and neighborhood score. The numbers will vary, e.g., 2,500 sq ft, 3 bedrooms, 2 miles to the center, and 75 score. We can set up the real-life implementation tool using scikit-learn model with StandardScaler:

    from sklearn.preprocessing import StandardScaler
    import numpy as np

    # Example data: size, rooms, distance, neighborhood score
    X = np.array([[2000, 3, 5, 80], 
              [1500, 2, 20, 60],
              [3000, 4, 10, 90]])

    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)

    print("Normalized Data:\n", X_normalized)

And then we get the results below:

    [[-0.26726124,  0.        , -1.06904497,  0.26726124],
     [-1.06904497, -1.22474487,  1.33630621, -1.33630621],
     [ 1.33630621,  1.22474487, -0.26726124,  1.06904497]]

After normalization, we now have: 
* Size feature: between -2 and 3
* Number of rooms: -1 and 2
* Distance: -1.5 and 2
* Score: -2 and 2 
