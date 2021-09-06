# Loosely following https://www.youtube.com/watch?v=ntKn5TPHHAk&list=PLRqwX-V7Uu6aCibgK1PTWWu9by6XFdCfh&index=2
#
import numpy as np
import random as rnd

# preceptron class as simple as it gets.


class Preceptron:
    def __init__(self, numWeights: int, learningRate: int):
        self.weights = []
        self.LR = learningRate
        for i in range(numWeights):
            self.weights.append(rnd.randrange(-1, 1))

    # actual operational methods

    def guess(self, inputs: list):
        return 1 if np.dot(inputs, self.weights) >= 0 else -1

    def train(self, inputs: list, target: int):
        guess = self.guess(inputs)
        error = target - guess
        # tune all the weights
        for i in range(len(self.weights)):
            self.weights[i] += error*inputs[i]
