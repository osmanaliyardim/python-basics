# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:14:29 2019

@author: Osman Ali Yardım

Dynamic Array with Python
"""

import ctypes # to create a new array

class DynamicArray(object):
    
    #initializer (constructor)
    def __init__(self):
        self.n = 0 # number of elements
        self.capacity = 1 # capacity
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        """
        return number of elements in array
        """
        return self.n
    
    def __getItem__(self,x):
        """
        return any element of the array
        """
        if not 0 <= x < self.n:
            return IndexError("X is out of bounds!")
        
        return self.A[x]
    
    def append(self,element):
        """
        add an element to the array
        """
        # for dynamic arrays, we increase capacity as double each time
        if self.n == self.capacity:
            self._resize(2*self.capacity) # make capacity of the array x2
        
        self.A[self.n] = element # add the element
        self.n += 1 # increase number of elements +1
        
    def _resize(self,new_cap):
        """
        increase capacity of the array
        """
        
        B = self.make_array(new_cap) # create a new array
        
        for i in range(self.n):
            B[i]=self.A[i] # assign values to our new array
            
        # Update elements in constructor for a new start
        self.A = B
        self.capacity = new_cap
        
    def make_array(self,new_cap):
         """
         return new array
         """
         return (new_cap*ctypes.py_object)()
     

# Demo for dynamic array usage
arr = DynamicArray()

arr.append(1)
print(arr.__getItem__(0))

arr.append(3)
print(arr.__getItem__(0), arr.__getItem__(1))

arr.append(5)
print(arr.__getItem__(0), arr.__getItem__(1), arr.__getItem__(2))

print(arr.__len__)