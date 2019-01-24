# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:29:24 2019

@author: Osman Ali Yardım

Sequential (Linear) Search with Unordered and Ordered List
"""

def seqSearchUnorderedList(liste, value):
    """
    Sequential (Linear) Search with Unordered List
    """
    index = 0
    found = False
    
    while index < len(liste) and not found:
        if liste[index] == value:
            found = True
        else:
            index += 1
    
    return (found,index)


#Demo for Sequential (Linear) Search with Unordered List
liste = [5,7,2,3,15,8,100,12]

found, index = seqSearchUnorderedList(liste, 15)
print(found)
print(index)

found2, index2 = seqSearchUnorderedList(liste, 11)
print(found2)
print(index2)

print("--------")

def seqSearchOrderedList(liste, value):
    """
    Sequential (Linear) Search with Ordered List
    """
    index = 0
    found = False
    stop = False
    
    while index < len(liste) and not found and not stop:
        if liste[index] == value:
            found = True
        else:
            if value < liste[index]:
                stop = True
            else:
                index += 1
    
    return (found,index)


#Demo for Sequential (Linear) Search with Ordered List
liste = [2,3,5,7,8,12,15,100]

found3, index3 = seqSearchOrderedList(liste,7)
print(found3)
print(index3) 

found4, index4 = seqSearchOrderedList(liste,10)
print(found4)
print(index4)