# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:57:07 2019

@author: Osman Ali Yardım

Merge Sort with Python
"""

def mergeSort(arr):
    """
    merge sort for unordered lists/arrays
    """
    
    if len(arr) > 1:
        
        mid = int(len(arr)/2) # Get middle value to divide arr
        
        lefthalf = arr[:mid] # Take leftside of arr
        righthalf = arr[mid:] # Take rightside of arr
        
        mergeSort(lefthalf) # Use recursion to continue to divide into single pieces
        mergeSort(righthalf)
    
        i=0 # for right half
        j=0 # for left half
        k=0 # to assign values to the new ordered arr
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    
    return arr


# Demo for Merge Sort
arr = [3,2,13,4,6,5,7,8,20]
print(mergeSort(arr))
