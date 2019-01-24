# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:15:52 2019

@author: Osman Ali Yardım

Doubly Linked List with Python
"""

class dllNode(object):
    
    def __init__(self,value):
        """
        Initialize constructor
        """
        self.value = value
        self.next = None
        self.prev = None
    
    def setNext(self,node):
        """
        To connect the next node
        """
        self.next = node
        
    def setPrev(self,node):
        """
        To connect the previous node
        """
        self.prev = node
        
    def getNext(self):
        """
        To return the next node
        """
        return self.next
    
    def getPrev(self):
        """
        To return the previous node
        """
        return self.prev
    
    def getValue(self):
        """
        To get the value of node
        """
        return self.value
    

# Demo for Doubly Linked List
ankara = dllNode("06")
izmir = dllNode("35")
istanbul = dllNode("34")

ankara.setNext(izmir) # ankara -> izmir
izmir.setNext(istanbul) # izmir -> istanbul
# ankara -> izmir -> istanbul
print(ankara.getNext().getValue())
print(izmir.getNext().getValue())
print(ankara.getNext().getNext().getValue())

print("------------")

istanbul.setPrev(izmir) # istanbul -> izmir
izmir.setPrev(ankara) # izmir -> ankara
# ankara <- izmir <- istanbul
print(istanbul.getPrev().getValue())
print(izmir.getPrev().getValue())
print(istanbul.getPrev().getPrev().getValue())
    