# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        #base case

        if not root:
            return
        
        def dfs(path, node):
            path = path + str(node.val)

            if node.left:
                dfs(path, node.left) 
            if node.right:
                dfs(path, node.right)
            
            if not (node.left or node.right):
                self.res += int(path)

        dfs("", root)
        return self.res 