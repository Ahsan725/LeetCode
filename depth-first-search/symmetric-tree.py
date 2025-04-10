# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_vals = []
            
            # Collect the entire level
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    # Use a placeholder for None
                    level_vals.append(None)
            
            # Check if level_vals is symmetrical
            if level_vals != level_vals[::-1]:
                return False
        
        return True

