import pandas as pd
from data_preprocessing_workout import preprocess_data
from model_training_workout import train_model

# Sample data
data = {
    'age': [25, 40, 35],
    'weight': [60, 80, 70],
    'availability': [5, 7, 3],
    'fitness_level': ['beginner', 'intermediate', 'advanced'],
    'goal': ['weight loss', 'muscle gain', 'endurance improvement']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Preprocess data
X = preprocess_data(df)

# Train model
predicted_probabilities = train_model(X.values.T)

print("Predicted probabilities:\n", predicted_probabilities)
