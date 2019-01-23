# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:18:28 2019

@author: Osman Ali Yardım

Stack with Python
"""

class Stack:
    
    def __init__(self):
        """
        Building initializer (constructor)
        """
        self.items = []
    
    def isEmpty(self):
        """
        Checks that stack is empty or not
        """
        return self.items == [] # boolean operation
    
    def push(self, item):
        """
        To add an item into stack
        """
        self.items.append(item)
    
    def pop(self):
        """
        To remove an item from stack
        """
        self.items.pop()
    
    def top(self):
        """
        To see the last item in stack
        """
        return self.items[len(self.items)-1]
    
    def size(self):
        """
        To get the size of stack
        """
        return len(self.items)
    

# Demo for creating a Stack
stack = Stack()
print(stack.isEmpty())

stack.push("London")
print(stack.top())

stack.push("Paris")
stack.push("Istanbul")
stack.push("Berlin")
print(stack.items)

print(stack.size())

stack.pop()
print(stack.top())

print(stack.size())
print(stack.isEmpty())