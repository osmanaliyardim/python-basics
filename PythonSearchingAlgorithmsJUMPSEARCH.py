# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:11:16 2019

@author: Osman Ali Yardım

Jump Search with Python
"""

import math

def jumpSearch(liste,value):
    """
    jump search for sorted arrays
    """
    n = len(liste)
    step = int(math.sqrt(len(liste)))
    found = False
    counter = 0
    
    for i in range(0,n,step):
        if liste[i] == value:
            found = True
        else:
            if value < liste[i]:
                print("Stopped index:", counter)
                break
        counter += step
        
    for j in range((counter-step)+1, counter):
        if liste[j] == value:
            found = True
    
    return found

# Another Jump Search Solution
def jumpSearch2(liste,value):
    """
    jump search for sorted arrays
    """
    n = len(liste)
    step = math.sqrt(n)
    prev = 0
    
    while liste[int(min(step,n)-1)] < value:
        prev = step
        step += math.sqrt(n)
        
        if prev >= n:
            return -1
    
    while liste[int(prev)] < value:
        prev += 1
        
        if prev == min(step,n):
            return -1
    
    if liste[int(prev)] == value:
        return int(prev)
    
    return -1


# Demo for Jump Search solutions
liste = [0,1,2,3,4,5,6,7,8] 
print(jumpSearch(liste,5)) # Jump Search Solution 1
print("----")
print(jumpSearch2(liste,5)) # Jump Search Solution 2