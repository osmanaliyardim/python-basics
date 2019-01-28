# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:33:38 2019

@author: Osman Ali Yardım

Deep First Search with Python
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


def deepFS(graph,start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop() # using pop to remove last item for DFS
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# Demo for Deep First Search
print(deepFS(graph,"A"))