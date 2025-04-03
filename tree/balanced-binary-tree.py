# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            #base case
            if not root:
                return [True, 0] #return true  = balanced and height of 0

            left = dfs(root.left) #this will get the height and check if balanced
            right = dfs(root.right) #same for right 
            
            #check if the balanced variable will be True or False for curr Node
            balanced = left[0] and right [0] and (abs(left[1] - right[1]) <= 1)

            #return true or false and the height of the tree until this node
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]