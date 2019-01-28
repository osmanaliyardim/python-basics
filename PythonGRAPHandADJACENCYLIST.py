# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:02:20 2019

@author: Osman Ali Yardım

Graph and Adjacency List Implementation with Python
"""

class Vertex:
    def __init__(self,key):
        """
        initialize constructor
        """
        self.value = key
        self.connectedTo = {}
        
    def addNeighbor(self,neighbor,weight=0):
        self.connectedTo[neighbor] = weight
        
    def printNode(self):
        return str(self.value) + " connected to: "+ str([x.value for x in self.connectedTo]) # List compherensions to get different values
    
    def getConnections(self):
        return self.connectedTo.keys() # get keys of dictionary (connectedTo)
    
    def getValue(self):
        return self.value
    
    def getWeight(self,neighbor):
        return self.connectedTo[neighbor]
    

class Graph:
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices += 1
        
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        
        return newVertex
    
    def getVertex(self,n):
        if n is self.vertList:
            return self.vertList[n]    
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,fromN,toN,cost=0):
        if fromN not in self.vertList:
            self.addVertex(fromN)
        if toN not in self.vertList:
            self.addVertex(toN)
        self.vertList[fromN].addNeighbor(self.vertList[toN],cost)
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    

# Demo for graph and adjacenct matrix
g = Graph()

g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
print(g.vertList)
print("--")

g.addEdge(1,2,0)
g.addEdge(1,3,0)
g.addEdge(5,3,0)

for v in g:
    print(v)
    print(v.getConnections())