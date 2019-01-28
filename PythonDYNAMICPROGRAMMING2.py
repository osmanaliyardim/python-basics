# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:01:56 2019

@author: Osman Ali Yardım

Dynamic Programming with Python
"""

def dynamicCatalan(n):
    
    # base case
    if n <= 1:
        return 1
    
    # storing
    catalan = [0 for i in range(n+1)] # list compherension
    
    # initialize first 2 values
    catalan[0], catalan[1] = 1,1
    
    # fill the list
    for i in range(2,n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j]*catalan[i-j-1]
    
    return catalan[i]


# Demo for Catalan Numbers with Dynamic Programming
for i in range(10):
    print(dynamicCatalan(i))