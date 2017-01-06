# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:21:17 2016

@author: Mark
"""
import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    num_result = 0
    for trial in range(0,numTrials):
        bucket = [0,0,0,1,1,1]
        del bucket[random.randint(0,5)]
        del bucket[random.randint(0,4)]
        del bucket[random.randint(0,3)]
        if bucket == [0,0,0] or bucket == [1,1,1]:
            num_result += 1
    return num_result / numTrials

print(noReplacementSimulation(1000000))