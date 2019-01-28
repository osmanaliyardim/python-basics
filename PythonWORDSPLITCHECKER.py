# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:39:10 2019

@author: Osman Ali Yardım

Word Split with Arrays
"""

def wordSplitChecker(liste):
    # Word example: "deeplearning"
    # List example: ["deeplearning", "d,dll,a,deep,base,layer,lear,learning"]
    word = list(liste[0]) # example: "d"
    otherwords = liste[1].split(",") # example: ["d", "dll", "a", "deep", "base", "layer", "lear", "learning"]
    
    for i in range(1,len(word)):
        word1 = word[:]
        word1.insert(i," ")
        
        x, y = "".join(word1).split() # "d", "eeplearning"
        
        if x in otherwords and y in otherwords: # if splited words are there in otherwords
            return x + ", " + y # return x and y
    
    return "Could not find any combine" # if splited words are not there in otherwords
    

# Demo for wordSplitChecker method
list1 = ["deeplearning", "d,dll,a,deep,base,layer,lear,learning"]
list2 = ["artificial", "art,ficial,math,lab,base,learning,deep"]
list3 = ["artificialintelligence", "art,d,a,dll,artificial,base,learning,intelligence"]

print(wordSplitChecker(list1))
print(wordSplitChecker(list2))
print(wordSplitChecker(list3))
