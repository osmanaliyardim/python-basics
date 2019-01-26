# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 13:19:05 2019

@author: Osman Ali Yardım

Counting Sort with Python
"""

def countingSort(array,maxval):
    """
    counting sort for unordered lists/arrays
    values must be in range (1,9)
    """
    
    m = maxval + 1
    count = [0] * m # [0,0,0...,0]

    for a in array:
        count[a] += 1
    
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    
    return array
    
# Demo for Counting Sort
arr = [1,2,3,4,5,6,7,7,7,7,1,1,1,2,3]
print(countingSort(arr,7))