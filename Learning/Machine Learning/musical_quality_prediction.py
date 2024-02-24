# Importing necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Sample data: musical chords and their corresponding qualities
chords = np.array([(1, 3, 5, 7, 0), (1, 3, 5, 6.5, 0), (1, 2.5, 5, 0, 0), (1, 2.5, 4.5, 0, 0), (1, 3, 5, 7, 9), (1, 2.5, 0, 0, 0), (1, 1.5, 0, 0, 0), (1, 3, 0, 0, 0), (1, 0, 5, 0,0), (1, 0, 4, 0, 0), (1, 0, 6, 0, 0), (1, 0, 0, 7, 0)])
qualities = np.array(["spheric", "dominant", "sad", "unstable", "colorful", "unstable", "unstable", "consonant", "consonant", "consonant", "consonant", "consonant"])

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(chords, qualities, test_size=0.2, random_state=42)

# Apparently linear regression doesn't work here because it expects continues values
# Instead logistic regression can be used for classification tasks
model = LogisticRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
predictions = model.predict(X_test)

# Printing the predictions
print("Predictions:", predictions)

# Can't use score to evaluate here as accuracy is more suitable for classification tasks
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)