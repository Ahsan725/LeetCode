# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        if not root:
            return res
        q = deque([(root, float('inf'))])

        while q:
            node, maxsofar = q.popleft()
            if node.val >= maxsofar:
                res += 1
            if node.right:
                q.append((q.right, max(maxsofar, node.val)))
            if node.left:
                q.append((q.left, max(maxsofar, node.val)))
        return res 