"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # two main pointers: first and last node in traversal
        if not root:
            return None

        self.first = None
        self.last = None 

        def inorder_link(node):
            if node:
                inorder_link(node.left)

                if self.last is None:
                    self.first = node
                    self.last = node
                else:
                    # correct link setup
                    self.last.right = node
                    node.left = self.last
                    self.last = node

                inorder_link(node.right)

        inorder_link(root)

        # Make it circular
        self.first.left = self.last
        self.last.right = self.first

        return self.first

        
        
        #two main variables first, last 
        if not root:
            return None
        
        self.first = None
        self.last = None 
        def inorder_link(node):
            if node:
                inorder_link(node.left)
                
                if self.last == None:
                    self.first = node
                    self.last = node
                else:
                    #set up the links
                    self.first.left = self.last
                    self.last.right = self.first
                    self.last = node
                    
                inorder_link(node.right)
        inorder_link(root)
        
        #not sure about which one is the left or right
        self.first.right = self.last
        self.last.left = self.first
        
        return self.first