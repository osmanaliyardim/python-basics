# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:31:23 2019

@author: Osman Ali Yardım

Step Counting with Recursion (A Google Interview Question)
"""

"""
Question: Suppose that you want climb a staircase of N steps, and on each step you can take either 1 or 2 steps.
How many distinct ways are there to climb the staircase? 
For example, if you wanted to climb 4 steps, you can take the following distinct number of steps;
1) 1,1,1,1
2) 1,1,2
3) 1,2,1
4) 2,1,1
5) 2,2
"""

def countSteps(n):
    
    #base case 1
    if n == 1:
        return 1
    
    #base case 2
    if n == 2:
        return 2
    
    return countSteps(n-1) + countSteps(n-2)


# Demo for countSteps
print(countSteps(4))