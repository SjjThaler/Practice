# Importing necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data: house sizes (in square feet) and their corresponding prices (in thousands of dollars)
chords = np.array([(1,3,5,7), (1,3,5,6.5), (1,2.5,5), (1,2.5,4.5), (1,3,5,7,9)]).reshape(-1, 1)  # Reshape to make it a 2D array
qualities = np.array(["spheric", "dominant", "sad", "unstable", "colorful"])

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(chords, qualities, test_size=0.2, random_state=42)

# Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
predictions = model.predict(X_test)

# Printing the predictions
print("Predictions:", predictions)

# Evaluating the model (optional)
score = model.score(X_test, y_test)
print("Model Score:", score)