# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 09:43:13 2016

@author: Mark
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    variance = 0
    L2 = []
    if len(L) == 0:
        return float('NaN')
    for string in L:
        L2.append(len(string))
    mean = sum(L2) / len(L2)
    for element in L2:
        variance += (element - mean)**2
    return (variance / len(L2))**.5 / ((sum(L2) / len(L2)))
    
L = ['aaaaaaaaaa','aaaa','aaaaaaaaaaaa','aaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaa','aaaaa']

print(stdDevOfLengths(L))