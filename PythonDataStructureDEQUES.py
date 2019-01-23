# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:40:09 2019

@author: Osman Ali Yardım

Deque with Python
"""

class Deque:
    
    def __init__(self):
        """
        Initialize constructor
        """
        self.items = []
        
    def isEmpty(self):
        """
        Check that deque is empty or not
        """
        return self.items == []
    
    def addRear(self, item):
        """
        To add an item into deque to the rear
        """
        self.items.insert(0,item)
        
    def addFront(self, item):
        """
        To add an item into deque to the head
        """
        self.items.append(item)
        
    def removeFront(self):
        """
        To remove the item from head of deque
        """
        return self.items.pop()
    
    def removeRear(self):
        """
        To remove the item from rear of deque
        """
        return self.items.pop(0)
    
    def size(self):
        """
        To get the size of deque
        """
        return len(self.items)
    

# Demo for Deque
deque = Deque()

print(deque.isEmpty())

deque.addFront("Berlin")
deque.addFront("Istanbul")
deque.addRear("London")

print(deque.isEmpty())
print(deque.items)

print(deque.removeFront())
print(deque.removeRear())

print(deque.items)
print(deque.size())     