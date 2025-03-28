# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = deque([root])  # Initialize the queue with the root node
        while q:
            # level_size = len(q)
            level_nodes = []  # Store nodes in the current level

            for i in range(len(q)):
                node = q.popleft()
                level_nodes.append(node.val) #add the node value to level_nodes

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_nodes: #if the level_nodes list is not empty
                res.append(level_nodes[-1]) #append the last value of the level to the result array.

        return res