# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #pre means root, left, right
        #stack [ 8, 9]
        #res =[1, 2, 4, 5, 6, 7, 3, 8, 9]

        res = []
        if not root:
            return res
        stack = [root]

        while stack:
            curNode = stack.pop()
            res.append(curNode.val)

            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)
        return res 