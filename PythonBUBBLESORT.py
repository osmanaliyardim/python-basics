# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:49:08 2019

@author: Osman Ali Yardım

Bubble Sort with Python
"""

def bubbleSort(arr):
    """
    bubble sort solution for unordered lists/arrays
    """
    
    for i in range(len(arr)-1,0,-1):
        
        for j in range(i):
            
            if arr[j] > arr[j+1]: # If the next value is greater than current, swap them
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


# Demo for Bubble Sort
arr = [3,2,13,4,6,5,7,8,20]
print(bubbleSort(arr))