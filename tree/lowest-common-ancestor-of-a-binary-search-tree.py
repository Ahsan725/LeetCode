# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            #only one of these will hit so adjust the cur value 
            
            #where the current root is bigger than both p and q value -> search the left
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left

            #where the current root is smaller than both p and q value -> search the right 
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            #return the current because split happening 
            else:
                return cur

