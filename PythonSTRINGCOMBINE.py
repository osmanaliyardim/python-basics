# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:46:09 2019

@author: Osman Ali Yardım

String Combinations (A Google Interview Question)
"""

"""
Question: The input will be a string consisting only of the characters 0, 1 and ?, where the ? acts as a wildcard
that can be either a 0 or 1. and your is to print all possible combinations of the string. For example,
if the string "011?0" then your program should output a set of all strings, which are: ["01100","01110"]
"""

def strCombine(string):
    
    strList = list(string)
    strList2 = list(string)
    
    # To change ? to 0
    for i in range (0, len(strList)):
        
        if strList[i] == '?':
            strList[i] = '0'
            
    string1 = "".join(strList)
    
    # To change ? to 1
    for j in range (0, len(strList2)):
        if strList2[j] == '?':
            strList2[j] = '1'
    
    string2 = "".join(strList2)
    
    finalList = [string1,string2]
    
    return finalList


# Demo for strCombine
print(strCombine("011?0"))