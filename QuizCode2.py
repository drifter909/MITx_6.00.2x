# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:20:02 2016

@author: Mark
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    remaining_summation = s
    list_of_coefficients = []
    for element in L:
        i = 0
        while (i+1)*element <= remaining_summation:
            i += 1
        list_of_coefficients.append(i)
        remaining_summation -= i*element
        
    if remaining_summation == 0:
        return sum(list_of_coefficients)
    else:
        return "no solution"
    
    

L = 10,4
s = 23
print(greedySum(L,s))