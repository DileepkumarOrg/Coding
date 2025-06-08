from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define hyperparameter grid
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [10, 20, None],
    "min_samples_split": [2, 5, 10]
}

# Grid Search for best parameters
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring="accuracy", n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)

# Get best model and accuracy
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test_scaled)
improved_accuracy = accuracy_score(y_test, y_pred_best)

print("Best Parameters:", grid_search.best_params_)
print("Improved Accuracy:", improved_accuracy)
