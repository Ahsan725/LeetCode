# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            #null node? 
            if not node:
                return 0
            
            return 1 + dfs(node.left) + dfs(node.right)
            #dfs on left: 4, 5, 2, root = 3
            #dfs on right: 6, 3, root = 2
        
        return dfs(root)