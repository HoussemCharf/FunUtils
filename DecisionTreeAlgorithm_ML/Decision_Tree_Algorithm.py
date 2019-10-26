# Decision Tree Classification

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('diabetes.csv')
X = dataset.iloc[:, :8].values
y = dataset.iloc[:, 8].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Fitting Decision Tree Classification to the Training set
from sklearn import tree
classifier = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
tree.export_graphviz(classifier)
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)

from sklearn.metrics import classification_report
cr=classification_report(y_test, y_pred)

import pydotplus
from IPython.display import Image
dot_data = tree.export_graphviz(classifier,out_file="resume.dot")
graph = pydotplus.graphviz.graph_from_dot_file("resume.dot")
graph.write_png('abc.png')
Image(graph.create_png())