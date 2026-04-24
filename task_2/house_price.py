# ================================
# 0. Fix matplotlib (Linux/WSL)
# ================================
import matplotlib
matplotlib.use('Agg')

# ================================
# 1. Import Libraries
# ================================
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# ================================
# 2. Load Dataset
# ================================
df = pd.read_csv("housing.csv")

print("First 5 rows:\n", df.head())

# ================================
# 3. Preprocessing
# ================================

# Convert categorical (location) → numeric
df = pd.get_dummies(df, columns=["location"], drop_first=True)

# Features and Target
X = df.drop("price", axis=1)
y = df["price"]

# ================================
# 4. Train-Test Split
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 5. Train Model
# ================================
model = LinearRegression()
model.fit(X_train, y_train)

# ================================
# 6. Prediction
# ================================
pred = model.predict(X_test)

# ================================
# 7. Evaluation
# ================================
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

print("\nModel Performance:")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# ================================
# 8. Save Results Table
# ================================
results = pd.DataFrame({
    "Actual_Price": y_test.values,
    "Predicted_Price": pred
})

results["Error"] = results["Actual_Price"] - results["Predicted_Price"]
results["Percentage_Error"] = (results["Error"] / results["Actual_Price"]) * 100

results.to_csv("prediction_results.csv", index=False)

print("\nSaved: prediction_results.csv")

# ================================
# 9. Visualization
# ================================
plt.scatter(y_test, pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.savefig("fig_regression.png")

print("Saved: fig_regression.png")