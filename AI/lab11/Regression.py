from math import exp, log
from numpy.linalg import inv
import numpy as np


def sigmoid(x):
    return 1 / (1 + exp(-x))


class MyLogisticRegression:
    def __init__(self):
        self.coef_ = []
        self.classifiers = []

    # simple stochastic GD
    def train_binary(self, inputs, outputs, learning_rate=0.0001, no_epochs=100):
        self.coef_ = [0.0 for _ in range(len(inputs[0]) + 1)]
        # self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]
        for epoch in range(no_epochs):
            #np.random.shuffle(inputs)
            for i in range(len(inputs)):  # for each sample from the training data
                y_computed = self.evaluate(inputs[i], self.coef_)  # estimate the output
                crt_error = y_computed - outputs[i]  # compute the error for the current sample
                for j in range(0, len(inputs[0])):  # update the coefficients
                    self.coef_[j] = self.coef_[j] - learning_rate * crt_error * inputs[i][j]
                self.coef_[len(inputs[0])] = self.coef_[len(inputs[0])] - learning_rate * crt_error * 1

    #makes a classifier for each output and calculated the fitness for each output label individually
    def fit(self, x, y):
        output_names = list(set(y))
        for label in range(len(output_names)):
            train_outputs_label = self.split_by_label(y, label)
            self.train_binary(x, train_outputs_label, 0.001, 100)
            self.classifiers.append(self.coef_)

    #transforms the outputs in a list of 0 and 1's depenidng on the label (one vs all implementation)
    def split_by_label(self, y, label):
        train_outputs = y[:]
        for i in range(len(train_outputs)):
            if train_outputs[i] == label:
                train_outputs[i] = 1
            else:
                train_outputs[i] = 0
        return train_outputs


    #calculate the output based on the coeficients w0 w1... and the features x1,x2...
    def evaluate(self, xi, coef):
        yi = coef[-1]
        for j in range(len(xi)):
            yi += coef[j] * xi[j]
        return yi

    # for every testinput array calculate de the predicted value based on its classifier
    # return a list of all the predicted value for each input
    def predict(self, x):
        computed = []
        for i in range(len(x)):
            val = [self.predict_prob_sample(x[i], self.classifiers[label]) for label in
                   range(len(self.classifiers))]
            index = val.index(max(val))
            computed.append(index)
        return computed

    #sigmoid of the distribution
    def predict_prob_sample(self, x, coef=None):
        return sigmoid(self.evaluate(x, coef))