# Removed codecademylib3_seaborn import (not needed outside Codecademy)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

# Explore the DataFrame structure
print(df.head())
print("\nDataFrame info:")
print(df.info())

# 3. Get mean total production per year
prod_per_year = df.groupby('year')['totalprod'].mean().reset_index()
print("\nProduction per year:")
print(prod_per_year)

# 4. Create x (years) and reshape
x = prod_per_year['year'].values.reshape(-1, 1)

# 5. Create y (total production)
y = prod_per_year['totalprod'].values

# 6. Plot scatterplot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='gold', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Total Honey Production')
plt.title('Honey Production Over Time')
plt.tight_layout()
plt.show()

# 7. Create and fit linear regression model
regr = linear_model.LinearRegression()
regr.fit(x, y)

# 8. Print slope and intercept
print(f"\nSlope (coef_): {regr.coef_[0]}")
print(f"Intercept: {regr.intercept_}")

# 9. Create predictions
y_predict = regr.predict(x)

# 10. Plot scatterplot with regression line
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='gold', edgecolor='black', label='Actual')
plt.plot(x, y_predict, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Total Honey Production')
plt.title('Honey Production with Linear Regression')
plt.legend()
plt.tight_layout()
plt.show()

# 11. Predict future years (2013 to 2050)
X_future = np.array(range(2013, 2051)).reshape(-1, 1)

# 12. Predict future honey production
future_predict = regr.predict(X_future)

# 13. Plot future predictions
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='gold', edgecolor='black', label='Actual')
plt.plot(x, y_predict, color='red', linewidth=2, label='Regression Line')
plt.plot(X_future, future_predict, color='blue', linestyle='--', label='Future Prediction')
plt.xlabel('Year')
plt.ylabel('Predicted Honey Production')
plt.title('Future Honey Production Prediction (2013-2050)')
plt.legend()
plt.tight_layout()
plt.show()

# Print specific prediction for 2050
print(f"\nPredicted honey production in 2050: {future_predict[-1]:.2f}")