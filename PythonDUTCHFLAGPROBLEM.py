# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:25:05 2019

@author: Osman Ali Yardım

Dutch National Flag Problem
"""

def swap(arr,i1,i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    
def natFlag(arr):
    
    low = 0
    mid = 0
    high = len(arr)-1 # the last element in list
    
    while mid <= high:
        
        if arr[mid] == 0:
            swap(arr,low,mid)
            low += 1
            mid += 1
        
        elif arr[mid] == 2:
            swap(arr,mid,high)
            high -= 1
        
        elif arr[mid] == 1:
            mid += 1
    
    return arr


# Demo for natFlag
print(natFlag([2,0,0,1,2,1]))
print(natFlag([1,2,0,1,0,2]))