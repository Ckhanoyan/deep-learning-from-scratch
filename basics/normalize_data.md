# Normalizing Data 

What does "normalizing data" mean? Normalizing data in machine learning or deep learning is actually critical because it may improve the performance and stability of the model such as when using gradient-based optimization algorithms. For example, multiple features in real-world data have different scales like age from 0-100 and income from 0 to billions. Without normalizing data, this may affect the model. 

## Health Insurance Approval Prediction (Scenario)

Suppose that you try to predict whether or not you will be approved for your health insurance using the features. Features include below:
* Age (in years): 0 to 100
* Annual Income (in dollars): $0 to $500000
* Number of dependents: 0 to 10

How does normalization help with this information above? 

Suppose that you feed all of this RAW data into the machine learning model, what might happen is that the model may focus too much on annual income because its numbers are in the hundreds of thousands, while the number of dependents is small (that is when I now understand why normalization is necessary! Bingo.). Therefore, this inbalance will cause the model to prioritize income over other important features. 

Without normalization, gradient descent - the learning process - will struggle to find the right balance since it may take large steps due to big ranges (income) and tiny steps for smaller ones (other features.) It means... a lot of zigzagging. 

### How can we bring the features to a similar scale then? 

How do we want to bring age, income, and dependents to (0-1)? Try this code I just developed.

    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler

    # Example raw data (health insurance)
    data = {
    'Age': [25, 45, 35, 50, 60],
    'Annual_Income': [50000, 120000, 75000, 200000, 300000],
    'Number_of_Dependents': [1, 0, 2, 4, 3]
    }

    # Create a DataFrame 
    df = pd.DataFrame(data) 

    # Display the raw data 
    print("Raw Data: ")
    print(df)

    # initialize the MinMaxScaler 
    scaler = MinMaxScaler()

    # Apply normalization
    normalization_data = scaler.fit_transform(df) 

    # Create a DataFrame with normalized values 
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

    # Display the normalized data 
    print("\nNormalized Data: ")
    print(normalized_df)

    # Save the normalized data to a CSV file (optional)
    normalized_df.to_csv("normalized_health_insurance_data.csv", index=False)

    
Then, we get this. 

<img width="344" alt="image" src="https://github.com/user-attachments/assets/60e4d466-f588-4d34-ae3e-5b9407937725" />


    
