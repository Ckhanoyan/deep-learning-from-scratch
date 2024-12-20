import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def preprocess_data(data):
    # Normalize numerical features
    scaler = MinMaxScaler()
    data[['age', 'weight', 'availability']] = scaler.fit_transform(data[['age', 'weight', 'availability']])

    # One-hot encode categorical features
    encoder = OneHotEncoder(sparse=False)
    fitness_level_encoded = encoder.fit_transform(data[['fitness_level']])
    goal_encoded = encoder.fit_transform(data[['goal']])

    # Concatenate encoded features with the original DataFrame
    encoded_df = pd.DataFrame(fitness_level_encoded, columns=encoder.get_feature_names_out(['fitness_level']))
    data = pd.concat([data, encoded_df], axis=1)
    encoded_df = pd.DataFrame(goal_encoded, columns=encoder.get_feature_names_out(['goal']))
    data = pd.concat([data, encoded_df], axis=1)

    # Drop original categorical columns
    data.drop(['fitness_level', 'goal'], axis=1, inplace=True)

    return data
