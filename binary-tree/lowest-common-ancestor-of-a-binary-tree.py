# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #th common ancestor is where both nodes have the same parent
        #another case is where one of the child nodes is also the parent of another 

        #parent = root
        #left_child = root.left
        #right_child = root.right

        #if left_child == p and right_child == q
        #then parent is the ancestor

        if not root:
            return None 
        
    
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        
        if l and r:
            return root
        else:
            return l or r



        
        