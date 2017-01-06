# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:10:29 2016

@author: Mark
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    
    def longest_run_one_trial(die,numRolls):
        longest_run = 1
        current_run = 1
        rollList = []
        for roll in range(0,numRolls):
            rollList.append(die.roll())
            if len(rollList) > 1 and rollList[-1] == rollList[-2]:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 1
        return longest_run
    
    longest_runs = []
    for trial in range(0,numTrials):
        longest_runs.append(longest_run_one_trial(die,numRolls))
        
    makeHistogram(longest_runs,10,'length of longest run', 'frequency')
    return(sum(longest_runs) / len(longest_runs))
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))