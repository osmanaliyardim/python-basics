# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:20:09 2019

@author: Osman Ali Yardım

Python Problem Solving Challenge Work
"""

# 1) A program that checks given mixed/shuffled words to compare they are the same or not
def isWordShuffled(word1, word2):
    
    # Travel in word2 to have access
    for i in word2:   
        # Check each letter, are they same or not
        if i not in word1:
            return False
    return True


# 2) A program that finds the frequency of letters in a word
def findFrequency(word):
    
    i = 0
    final_word = ""
    
    # Access each letter in the word
    while i < len(word):
        c = word[i]
        j = i + 1
    
        compressed = [1,c] # Initialize counter
    
        while j < len(word):
            if word[j] == c: # Check the next value
                compressed[0] += 1 # If the next value is the same, then add +1 to counter
            else:
                break
            j += 1 # Check next value
        
        # example = [2,k] [3,c] => 2k3c...
        final_word += "".join(map(str,compressed)) # Combine/Join letters
        
        i = j
    
    return final_word # Return the final combined word


# 3) A program that finds the missing digit in a math problem
def missingDigit(word):
    
    for i in range(10): # 0,1,2...,9
        c = word.replace("x", str(i)) # Try all possibilities by replacing
        x = word.index("=") # Save index of =
        
        if eval(c[:x]) == eval(c[x+1:]): # Use eval() method to compare before/after of "="
            return str(i) # Return the value found


# 4) A program that rotates the given array/list according to the first value
def rotateArray(array):
    
    first_value = array[0]
    final_word = ""
    
    for i in range(first_value,len(array)):
        final_word += str(array[i])
    
    for i in range(0, first_value):
        final_word += str(array[i])
    
    return final_word


# 5) A program which checks "are there any pair values in a list/array or not"
def isPairArray(array):
    
    word = ""
    
    for i in range(len(array)):
        word += str(array[i]) + " " # "5 6"
        
        if i%2 == 1: # If we are at an even index
            word += "," # Append a comma to seperate pairs
    
    word = word.split(" ,") # ["5 6", "6 5", "3 3", ""]
    
    storage_list = []
    for i in word:
        if i[::-1] not in word: # Check the reverse pair exists or not
            for j in i.split():
                storage_list.append(j) # If reverse pair does not exist, then append it to storage list
        elif i == i[::-1] and word.count(i)<2:
            for j in i.split():
                storage_list.append(j)
    
    if storage_list == []: # If storage_list is empty that means there are pairs
        return "Pairs are confirmed"
    
    return ",".join(storage_list) # If storage_list is not empty, then write the values that have not a pair


# Demo part for program 1
word1 = "compareit"
word2 = "tompcaeri"
word3 = "nothing"

print(isWordShuffled(word1, word2))
print(isWordShuffled(word1, word3))
print(isWordShuffled(word3, word2))


# Demo part for program 2
word1 = "reenjoy"
word2 = "axxerare"
word3 = "aabbbcdddd"

print(findFrequency(word1))
print(findFrequency(word2))
print(findFrequency(word3))


# Demo part for program 3
mathOperation1 = "1x0/10=12"
mathOperation2 = "5*x=20"
mathOperation3 = "1x+2=12"

print(missingDigit(mathOperation1))
print(missingDigit(mathOperation2))
print(missingDigit(mathOperation3))


# Demo part for program 4
array1 = [4,3,5,6,7,10,11,12]
array2 = [2,11,100,220,300]

print(rotateArray(array1))
print(rotateArray(array2))


# Demo part for program 5
array1 = [3,6,6,3,9,5,5,9]
array2 = [3,4,4,3,1,2]
array3 = [1,2,3,4,4,3]
array4 = [4,5,3,9,9,3,5,4]

print(isPairArray(array1))
print(isPairArray(array2))
print(isPairArray(array3))
print(isPairArray(array4))