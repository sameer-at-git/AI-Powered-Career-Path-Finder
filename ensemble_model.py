import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a synthetic dataset for demonstration
data = {
    'skill_score': np.random.randint(1, 100, 100),
    'experience_years': np.random.randint(0, 10, 100),
    'suitable_role': np.random.choice([0, 1], 100)  # 0: Data Analyst, 1: Software Developer
}
df = pd.DataFrame(data)

# Define features and target
X = df[['skill_score', 'experience_years']]
y = df['suitable_role']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Prepare LightGBM datasets
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# Set LightGBM parameters
params = {
    'objective': 'binary',
    'metric': 'binary_error',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'verbose': 0
}

# Train the LightGBM model
model = lgb.train(params, train_data, num_boost_round=100, valid_sets=[test_data], early_stopping_rounds=10)

# Make predictions and evaluate
predictions = (model.predict(X_test, num_iteration=model.best_iteration) > 0.5).astype(int)
print("LightGBM Accuracy:", accuracy_score(y_test, predictions))
