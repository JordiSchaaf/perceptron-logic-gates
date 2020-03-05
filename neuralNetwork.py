# Author: Jordi Schaaf
#
# This example contains different logic gates, built using perceptrons
# Each perceptron needs a list of ones/zeros as input, except for the Not-gate

from perceptron import Perceptron

# Perceptron with only one value in the inputlist
# Not-gate
def Not(input):
    w = [-1]
    b = 1
    return Perceptron(input, w, b).calc()

# Perceptrons with two values in the inputlist
# And-gate
def And(input):
    w = [1,1]
    b = -1
    return Perceptron(input, w, b).calc()

# Or-gate
def Or(input):
    w = [2,2]
    b = -1
    return Perceptron(input, w, b).calc()

# Not-Or-gate
def Nor(input):
    w = [-1,-1]
    b = 1
    return Perceptron(input, w, b).calc()

# Not-And-gate
def Nand(input):
    w = [-1,-1]
    b = 2
    return Perceptron(input, w, b).calc()

# Exclusive-Not-Or-gate
def Xnor(input):
    return Or([And(input), Nor(input)])

# Exclusive-Or-gate
def Xor(input):
    return And([Or(input), Nand(input)])


# Example for using the And-gate
print(And([1,1]))
