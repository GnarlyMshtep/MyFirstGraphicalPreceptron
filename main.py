import random as rnd

from numpy.core.numeric import False_
from Point import Point
from Preceptron import Preceptron

import matplotlib.pyplot as plt
import numpy as np

# constants
NUM_TRAINING_POINTS = 100
NUM_TESTING_POINTS = 10
MAXNUM = 100
MINNUM = 0

NUM_TESTS = 10  # how many different preceptrons will we train and test?


def main():
    # create simple training data set
    precentRight = 0
    for i in range(NUM_TESTS):
        precentRight += trainAndTestPrecep(NUM_TRAINING_POINTS,
                                           NUM_TESTING_POINTS, MAXNUM, MINNUM, graph=(i % 4 == 0))
    print("Precentege of overall correct guesses by all preceptrons on", NUM_TESTING_POINTS,
          "testing pts and", NUM_TRAINING_POINTS, "training points is:", precentRight/NUM_TESTS)


def trainAndTestPrecep(NUM_TRAINING_POINTS, NUM_TESTING_POINTS, MAXNUM, MINNUM, graph: bool = False):
    numRight = 0
    p = Preceptron(2, .1)
    trainingPts = []
    testingPts = []

    for i in range(NUM_TRAINING_POINTS):
        trainingPts.append(
            Point([rnd.randint(MINNUM, MAXNUM), rnd.randint(MINNUM, MAXNUM)]))

    for i in range(NUM_TESTING_POINTS):
        testingPts.append(
            Point([rnd.randint(MINNUM, MAXNUM), rnd.randint(MINNUM, MAXNUM)]))

    # train preceptron
    for pt in trainingPts:
        p.train(pt.getCoords(), pt.getLabel())

    # testPreceptron
    guesses = []
    for pt in testingPts:
        guesses.append(p.guess(pt.getCoords()))
        if(pt.getLabel() == p.guess(pt.getCoords())):
            numRight += 1

    if(graph):
        visualizeWithGuess(testingPts, guesses)

    return numRight/NUM_TESTING_POINTS


"""
Correctly guessed points are colored green while misses are colored red :)
"""


def visualizeWithGuess(pts: list, guesses: list):
    plt.title(label="Trained on " + str(NUM_TRAINING_POINTS))
    for i in range(len(pts)):
        if(pts[i].getLabel() == guesses[i]):
            plt.scatter(x=pts[i].coords[0],
                        y=pts[i].coords[1], color='#BDF7B7')

        else:
            plt.scatter(x=pts[i].coords[0],
                        y=pts[i].coords[1], color='#6B2737')

    plt.show()


def visualizeNoGuess(pts: list):
    for pt in pts:
        if(pt.getLabel() == 1):
            plt.scatter(x=pt.coords[0], y=pt.coords[1], color='#BDF7B7')

        else:
            plt.scatter(x=pt.coords[0], y=pt.coords[1], color='#6B2737')

    plt.show()


if __name__ == "__main__":
    main()
