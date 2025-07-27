from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([6.1101, 5.5277, 8.5186, 7.0032, 5.8598]).reshape(-1, 1)
y = np.array([17.592, 9.1302, 13.662, 11.854, 6.8233])

# Train model
model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=-1)
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, color='red', label='Training data')
plt.plot(X, y_pred, color='blue', label='Prediction')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.title('Linear Regression using scikit-learn')
plt.legend()
plt.grid(True)
plt.show()
