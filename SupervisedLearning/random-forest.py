# This is a code example of using Random Forests with Scikit-learn
# The dataset used is the Iris dataset

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load in the data
data = load_iris()

# The data that will be used to train the Random Forest
train_data = data.data[:-5]
train_target = data.target[:-5]

# The data we'll use to test our trained Random Forest
test_data = data.data[-5:]
test_target = data.target[-5:]

# Create the Random Forest Classifier
# n_jobs will use as many threads as possible
clf = RandomForestClassifier(n_jobs=-1)

# Fit the model using the training data
clf.fit(train_data, train_target)

# Try predicting and see that the prediction matches what we wanted to get 
prediction = clf.predict(test_data)

print("Test Target:", test_target)
print("Prediction:", prediction)
