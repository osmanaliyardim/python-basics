# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:39:28 2019

@author: Osman Ali Yardım

Breadth First Search with Python
"""

# Creating our sample graph
graph = {"A":set(["B","C"]),
         "B":set(["A","D","E"]),
         "C":set(["A","F"]),
         "D":set(["B"]),
         "E":set(["B","F"]),
         "F":set(["C","E"])
         }

print(graph)


def breadthFS(graph,start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0) # using pop(0) to start removing from root to deep for BFS
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Demo for Breadth First Search
print(breadthFS(graph,"A"))