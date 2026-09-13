import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ============================================================
# LAB 5 - LINEAR REGRESSION: HOUSE PRICE KAGGLE SUBMISSION
# ============================================================

# 1. Load the Kaggle training and test datasets
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# 2. Select the same features used in the lab
features = [
    "GrLivArea",
    "OverallQual",
    "TotalBsmtSF",
    "GarageCars",
    "YearBuilt",
    "FullBath",
    "Neighborhood",
    "HouseStyle",
    "KitchenQual",
    "GarageType"
]

target = "SalePrice"

numeric_features = [
    "GrLivArea",
    "OverallQual",
    "TotalBsmtSF",
    "GarageCars",
    "YearBuilt",
    "FullBath"
]

categorical_features = [
    "Neighborhood",
    "HouseStyle",
    "KitchenQual",
    "GarageType"
]

# 3. Prepare training features and target
X = train_df[features].copy()
y = train_df[target].copy()

# 4. Fill missing values
# Numerical columns -> median
for col in numeric_features:
    X[col] = X[col].fillna(X[col].median())

# Categorical columns -> most common value
for col in categorical_features:
    X[col] = X[col].fillna(X[col].mode()[0])

# 5. One-hot encode categorical columns
X = pd.get_dummies(
    X,
    columns=categorical_features,
    drop_first=True
)

# Make sure all values are numeric
X = X.astype(float)

# 6. Split the data (80/20), as required by the lab
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# 7. Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully.")

# 8. Prepare Kaggle test data using the SAME features
X_kaggle = test_df[features].copy()

# Use training-data statistics for filling missing values
for col in numeric_features:
    X_kaggle[col] = X_kaggle[col].fillna(
        X[col].median()
    )

for col in categorical_features:
    X_kaggle[col] = X_kaggle[col].fillna(
        X[col].mode()[0]
    )

# 9. Encode categorical columns
X_kaggle = pd.get_dummies(
    X_kaggle,
    columns=categorical_features,
    drop_first=True
)

# 10. Make Kaggle test columns exactly match training columns
X_kaggle = X_kaggle.reindex(
    columns=X.columns,
    fill_value=0
)

X_kaggle = X_kaggle.astype(float)

# 11. Predict SalePrice for every Kaggle test row
predictions = model.predict(X_kaggle)

# 12. Create Kaggle submission file
submission = pd.DataFrame({
    "Id": test_df["Id"],
    "SalePrice": predictions
})

# 13. Save the submission
submission.to_csv("submission.csv", index=False)

# 14. Basic checks
print("\nSubmission created successfully!")
print("File: submission.csv")
print("Rows:", len(submission))
print("Columns:", list(submission.columns))

print("\nFirst 5 predictions:")
print(submission.head())

print("\nMissing values:")
print(submission.isnull().sum())

print("\nYou can now upload submission.csv to Kaggle.")
