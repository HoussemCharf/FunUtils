import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics


# -------------------------------------------------------------------------------------------------------- #
# A script using linear regression to estimate the grades of students in G3 based on their results in G1   #
# and G2 as well as their absences during the academic year, their failures and the time studied per week. #
#                                          Written by @tobinatore                                          #
#                                                                                                          #
#                                This script uses the following dataset:                                   #
#                       https://archive.ics.uci.edu/ml/datasets/Student+Performance                        #
# -------------------------------------------------------------------------------------------------------- #


def read_data(filename):
    """
    Function for reading the CSV-file and dropping all columns that aren't important for our purpose.
    :param filename: String
    :return: DataFrame
    """
    dat = pd.read_csv(filename, sep=";")
    dat = dat[["G1", "G2", "studytime", "failures", "absences", "G3"]]
    return dat


def r_squared(pred, res):
    """
    Calculating the R² score of this model.
    Value returned is between 0.0 and 1.0, the higher the better.
    :param pred: List<Int>
    :param res:  List<Int>
    :return: Float
    """
    ss_t = 0
    ss_r = 0

    for i in range(len(pred)):
        ss_t += (res[i] - statistics.mean(res)) ** 2
        ss_r += (res[i] - pred[i]) ** 2

    return 1 - (ss_r / ss_t)


def rmse(pred, res):
    """
    Calculating the Root Mean Square Error.
    The lower the returned value, the better.
    :param pred: List<Int>
    :param res:  List<Int>
    :return: Float
    """
    rmse = 0
    for i in range(len(pred)):
        rmse += (res[i] - pred[i]) ** 2
    return np.sqrt(rmse / len(pred))


def get_cost(X, y, theta):
    """
    Getting the cost using the current values of theta.
    :param X: numpy.ndarray
    :param y: numpy.ndarray
    :param theta: numpy.ndarray
    :return: Float
    """
    cost = np.power(((X @ theta.T)-y), 2)
    return np.sum(cost)/(2 * len(X))


def gradient_descent(X, y, theta, iterations, alpha):
    """
    Optimizing the values of theta using gradient descent.
    :param X: numpy.ndarray
    :param y: numpy.ndarray
    :param theta: numpy.ndarray
    :param iterations: Integer
    :param alpha: Integer
    :return: numpy.ndarray, numpy.ndarray
    """
    cost = np.zeros(iterations)
    for i in range(iterations):
        theta = theta - (alpha / len(X)) * np.sum(X * ((X @ theta.T) - y), axis=0)
        cost[i] = get_cost(X, y, theta)
    return theta, cost


data = read_data("student-mat.csv")

# Splitting the data in two batches.
# 70% training data, 30% test data
train = data.sample(frac=0.7)
test = data.drop(train.index)

# Preparing 2 numpy arrays.
# X will hold all data except G3 and y only holds G3
X = train.iloc[:, :5]
ones = np.ones([X.shape[0], 1])
X = np.concatenate((ones, X), axis=1)

y = train.iloc[:, -1:].values

# Initializing theta
theta = np.zeros([1, 6])

# Setting hyper parameters
alpha = 0.00001
iterations = 5000

# Training the model.
# This means optimizing the cost via gradient descent and calculating the final cost.
theta, cost = gradient_descent(X, y, theta, iterations, alpha)
final_cost = get_cost(X, y, theta)

# Plotting the cost in relation to the iteration
fig, ax = plt.subplots()
ax.plot(np.arange(iterations), cost, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()

print("Final cost: ", final_cost)

# Initializing the test set
X_test = test.iloc[:, :5].values.tolist()

y_test = test.iloc[:, -1:].values

theta = theta.tolist()

# Transforming y_test from [[10],[4],...,[20]] to a simple list [10, 4, ..., 20]
store = []
for entry in y_test.tolist():
    store.append(entry[0])

y_test = store.copy()

# Calculating predictions using the function theta1 + (theta2 * x1) + ... + (theta6 * x5)
predictions = []
for line in X_test:
    prediction = round(theta[0][0] + (theta[0][1]*line[0]) + (theta[0][2]*line[1]) + (theta[0][3]*line[2]) + \
                       (theta[0][4] * line[3]) + (theta[0][5]*line[4]))

    predictions.append(prediction)

# Printing the score of the model
print("RMSE-Score: ", rmse(predictions, y_test))
print("R²-Score:", r_squared(predictions, y_test))

