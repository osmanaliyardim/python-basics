# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:29:12 2019

@author: Osman Ali Yardım

Queue with Python
"""

class Queue:
    
    def __init__(self):
        """
        Initialize constructor
        """
        self.items = []
    
    def isEmpty(self):
        """
        Check that queue is empty or not
        """
        return self.items == [] # boolean operation
    
    def enqueue(self, item):
        """
        To add an item into queue
        """
        self.items.insert(0,item) # To add an item to the head
    
    def dequeue(self):
        """
        To delete the first item in queue
        """
        return self.items.pop()
        
    def size(self):
        """
        To see the size of queue
        """
        return len(self.items)


# Demo for Queue
queue = Queue()

print(queue.isEmpty())

queue.enqueue("London")
queue.enqueue("Istanbul")
print(queue.size())
print(queue.isEmpty())

queue.dequeue()
print(queue.size())

queue.dequeue()
print(queue.isEmpty())