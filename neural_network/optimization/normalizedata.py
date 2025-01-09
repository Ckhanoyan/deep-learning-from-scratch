from sklearn.preprocessing import StandardScaler
import numpy as np

# Example data: size, rooms, distance, neighborhood score
X = np.array([[2000, 3, 5, 80], 
              [1500, 2, 20, 60],
              [3000, 4, 10, 90]])

scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

print("Normalized Data:\n", X_normalized)
