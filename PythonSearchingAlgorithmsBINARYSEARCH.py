# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:01:03 2019

@author: Osman Ali Yardım

Binary Search with Python
"""

def binarySearch(liste,value):
    """
    binary search for sorted arrays
    """
    first_index=0
    last_index = len(liste) - 1
    
    found = False
    
    while first_index <= last_index and not found:
        
        middle_index = int((first_index + last_index)/2)
        
        if liste[middle_index] == value: # also this can be added "or liste[first_index] == value or liste[last_index] == value"
            found = True
        else:
            # check lower half
            if value < liste[middle_index]:
                last_index = middle_index - 1
                print("lower half")
            
            # check upper half
            else:
                first_index = middle_index + 1
                print("upper half")
    
    return found


# Demo for Binary Search
liste = [3,6,11,12,18,21,34]
print(binarySearch(liste,18))