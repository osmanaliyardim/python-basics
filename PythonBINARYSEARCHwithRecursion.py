# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:31:54 2019

@author: Osman Ali Yardım

Binary Search with Recursion
"""

def binarySearchRec(arr, e):
    """
    binary search with recursion
    """
    
    # Base Case for Recursion
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:
        mid = int(len(arr)/2)
        if arr[mid] == e: # If we found
            return True
        else:
            # lower half
            if e < arr[mid]:
                return binarySearchRec(arr[:mid],e)
            
            # upper half
            else:
                return binarySearchRec(arr[mid+1:],e)


# Demo for Recursive Binary Search
liste = [3,6,11,12,18,21,34]
print(binarySearchRec(liste,18))
print("-----")
print(binarySearchRec(liste,40))
print("-----")
print(binarySearchRec(liste,2))