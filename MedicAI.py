# Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_selection import RFE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Loading the dataset
cancer = load_breast_cancer()

# Printing the first 5 rows of the dataset
print(cancer.data[:5])

# Accessing the column names
print(cancer.feature_names)

# Creating a DataFrame
data = pd.DataFrame(cancer.data, columns=cancer.feature_names)

# Adding the target column
data['target'] = cancer.target

# Visualizing the features
sns.pairplot(data, hue='target')
plt.tight_layout()
plt.show()

# Splitting the dataset
X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modeling
model = LogisticRegression(random_state=42)

# Performing Recursive Feature Elimination (RFE)
rfe = RFE(model, step=1)

# Fitting the model
rfe.fit(X_train_scaled, y_train)

# Selecting the optimal number of features
feature_names = X.columns[rfe.support_]
print(feature_names)

# Model training
model.fit(X_train_scaled[:, rfe.ranking_[:5]], y_train)

# Predicting the test dataset
y_pred = model.predict(X_test_scaled)

# Model evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))