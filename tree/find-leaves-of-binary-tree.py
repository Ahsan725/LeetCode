# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_map = defaultdict(list) #to store leaves based on removals 

        def dfs(node):
            if not node:
                return -1 #this should not contribute anything to the final rsult since the first lvl will be 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            height = max(left, right) + 1
            level_map[height].append(node.val)
            return height

        dfs(root)
        
        # Convert map to list of lists, ordered by level
        return [level_map[level] for level in sorted(level_map)]

