# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 09:52:57 2016

@author: Mark
"""

import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    posResult = 0
    for i in range(numTrials):
        chosen = []
        b=['r','r','r','r','g','g','g','g']
        for a in range(3):
          ball=random.choice(b)
          chosen.append(ball)
          b.remove(ball)
        if chosen[0]==chosen[1] and chosen[1]==chosen[2]:
            posResult += 1
    return float(posResult)/numTrials 
    
