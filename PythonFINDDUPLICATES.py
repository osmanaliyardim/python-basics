# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:14:12 2019

@author: Osman Ali Yardım

Finding Duplicates Numbers in a(n) List/Array
"""

def findDuplicates(list):
    
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                return "okay"
                break
    
    return "not"

# Demo for findDuplicates
print(findDuplicates([1,2,3,3]))