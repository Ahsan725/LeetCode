# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #iterate over the entire bst
        q = [root]
        values = []

        while q:
            node = q.pop()
            values.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        #values; [1,2,3,4,5,6] -> [1,2,3,4]
        #Time: Nlogn #Space: n
        values.sort()
        return values[k - 1]