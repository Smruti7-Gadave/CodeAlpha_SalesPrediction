import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("Advertising.csv")

print("First 5 rows:\n", df.head())
print("\nColumns:\n", df.columns)

# =========================
# DATA CLEANING
# =========================
df = df.dropna()

# =========================
# FEATURES & TARGET
# =========================
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# =========================
# SPLIT DATA
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# TRAIN MODEL
# =========================
model = LinearRegression()
model.fit(X_train, y_train)

# =========================
# PREDICT TEST DATA
# =========================
y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\nModel Performance:")
print("Accuracy (R2): {:.2f}%".format(r2 * 100))
print("MAE:", mae)

# =========================
# SAMPLE PREDICTIONS
# =========================
print("\nSample Predictions:")
for i in range(5):
    print("Actual:", y_test.iloc[i], "Predicted:", round(y_pred[i], 2))

# =========================
# VISUALIZATION 1
# =========================
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

# =========================
# VISUALIZATION 2
# =========================
importance = model.coef_

plt.bar(['TV', 'Radio', 'Newspaper'], importance)
plt.title("Impact of Advertising on Sales")
plt.ylabel("Impact Value")
plt.show()

# =========================
# 🔥 MANUAL INPUT PREDICTION
# =========================
print("\n--- Predict New Sales ---")

tv = float(input("Enter TV advertising budget: "))
radio = float(input("Enter Radio advertising budget: "))
news = float(input("Enter Newspaper advertising budget: "))

# FIX: Use DataFrame to remove warning
new_data = pd.DataFrame(
    [[tv, radio, news]],
    columns=['TV', 'Radio', 'Newspaper']
)

predicted_sales = model.predict(new_data)

print("\n📈 Predicted Sales:", round(predicted_sales[0], 2))