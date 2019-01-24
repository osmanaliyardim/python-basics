# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:03:38 2019

@author: Osman Ali Yardım

Linked List with Python
"""

class Node(object):
    
    def __init__(self,value):
        """
        Initialize constructor
        """
        self.value = value
        self.next = None
        
    def setNext(self,node):
        """
        to connect the next node
        """
        self.next = node
        
    def getNext(self):
        """
        to see what the next node is
        """
        return self.next
    
    def getValue(self):
        """
        to return the value of node
        """
        return self.value


# Demo for linkedlist
ankara = Node("06")
izmir = Node("35")
istanbul = Node("34")

# istanbul -> izmir -> ankara
istanbul.setNext(izmir) # istanbul -> izmir
izmir.setNext(ankara)  # izmir -> ankara

print(istanbul.getNext().getValue()) 
print(izmir.getNext().getValue())

print(istanbul.getNext().getNext().getValue()) # istanbul -> izmir -> ankara 