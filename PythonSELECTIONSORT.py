# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 13:14:38 2019

@author: Osman Ali Yardım

Selection Sort with Python
"""

def selectionSort(arr):
    """
    selection sort for unordered lists/arrays
    """
    
    for i in range(len(arr)-1,0,-1):
        positionOfMax = 0
        
        for location in range(1,i+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
        temp = arr[i]
        arr[i] = arr[positionOfMax]
        arr[positionOfMax] = temp
    return arr

# Demo for Selection Sort
arr = [3,2,13,4,6,5,7,8,20]
print(selectionSort(arr))