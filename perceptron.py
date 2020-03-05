# Author: Jordi Schaaf
#
# This perceptron takes as input:
#   - a list of n one(s)/zero(s)
#   - a list of n weights
#   - a bias
# And returns:
#   - An integer as activation

class Perceptron:
    def __init__(self, inputs, weights, bias):
        self.output = 0
        self.inputs = inputs
        self.weights = weights
        self.bias = bias

    def calc(self):
        for i in range(len(self.inputs)):
            self.output += self.inputs[i] * self.weights[i]
        self.output += self.bias

        return self.relu(self.output)

# Simple activation function that either returns 1 or 0
    def relu(self, input):
        return 1 if input > 0 else 0
