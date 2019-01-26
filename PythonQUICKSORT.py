# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 13:32:30 2019

@author: Osman Ali Yardım

Quick Sort with Python
"""

# recursive
def quickSort(arr):
    quickSortRec(arr,0,len(arr)-1)
    return arr

def quickSortRec(arr,first,last):
    
    if first < last:
        splitpoint = partition(arr,first,last)
        
        # Left right
        quickSortRec(arr,first,splitpoint-1)
        quickSortRec(arr,splitpoint+1,last)
        
def partition(arr,first,last):
    pivotValue = arr[first]
    
    left = first+1
    right = last
    
    done = False
    
    while not done:
        while left <= right and arr[left] <= pivotValue:
            left = left+1
        while arr[right] >= pivotValue and right >= left:
            right = right-1
        
        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    
    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp

    return right



# Demo for Quick Sort
arr = [3,2,13,4,6,5,734,4]
print(quickSort(arr))