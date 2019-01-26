# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 13:08:36 2019

@author: Osman Ali Yardım

Insertion Sort with Python
"""

def insertionSort(arr):
    """
    insertion sort for unordered lists/arrays
    """
    
    for i in range(1,len(arr)):
        
        currentValue = arr[i]
        position = i
        
        # Sublist
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position -= 1
            
        arr[position] = currentValue
    
    return arr

# Demo for Insertion Sort
arr = [3,2,13,4,6,5,7,8,20]
print(insertionSort(arr))