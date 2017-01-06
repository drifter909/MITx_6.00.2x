# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:40:16 2016

@author: Mark
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_sum = 0
    best_list = []
    for ind in range(0,len(L)+ 1):
        for ind2 in range(0,len(L) + 1):
            if ind <= ind2:
                if sum(L[ind:ind2]) > max_sum:
                    best_list = L[ind:ind2]
                    max_sum = sum(best_list)
    return best_list
    
