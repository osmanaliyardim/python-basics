# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 08:51:29 2019

@author: Osman Ali Yardım

Dynamic Programming with Python
"""

def dynamicFibo(n):
    """
    a method that returns Nth fibonnaci value with dynamic programming
    """
    fiboList = [0,1]
    
    while len(fiboList) < n+1:
        fiboList.append(0)
    
    #base case
    if n <= 1:
        return n
    else:
        if fiboList[n-1] == 0:
            fiboList[n-1] = dynamicFibo(n-1)
        if fiboList[n-2] == 0:
            fiboList[n-2] = dynamicFibo(n-2)
        
        fiboList[n] = fiboList[n-2] + fiboList[n-1]
    
    return fiboList[n]


# Demo for Dynamic Programming
print(dynamicFibo(8))