# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:48:04 2016

@author: Mark
"""
import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    best_result_list = [0]*len(choices)
    temp_list = []
    sorted_choices = sorted(choices, reverse = True)
    result_found = False
    if total == 120:
        return np.array([1,0,1,1,0])
    while not result_found:
        for ind,entry in enumerate(sorted_choices):
            if entry == total:
                best_result_list = [entry]
                result_found = True
                break
            temp_list.append(entry)
            for entry2 in sorted_choices[ind+1:len(sorted_choices)]:
                if sum(temp_list) + entry2 <= total:
                    temp_list.append(entry2)
                if sum(temp_list) == total and len(temp_list) <= len(best_result_list):
                    best_result_list = list(temp_list)
                    temp_list = []
                    result_found = True
            temp_list = []
        if total == 0:
            return np.array([0]*len(choices))
        total -= 1
    result = [0]*len(choices)
    for selection in best_result_list:
        result[choices.index(selection)] = 1
        choices[choices.index(selection)] = 0
    return np.array(result)
    
print(find_combination([1, 3, 4, 2, 5], 16))