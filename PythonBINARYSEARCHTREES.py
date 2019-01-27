# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:07:11 2019

@author: Osman Ali Yardım

Binary Search Tree with Python
"""

class Node:
    def __init__(self,key):
        """
        initialize constructor
        """
        self.val = key
        self.left = None
        self.right = None

        
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
    else:
        return None
    
    
    
# Demo for Binary Search Trees
r = Node(41)
insert(r,Node(65))
insert(r,Node(99))
insert(r,Node(50))
insert(r,Node(20))
insert(r,Node(11))
insert(r,Node(29))
insert(r,Node(51))
inorder(r)