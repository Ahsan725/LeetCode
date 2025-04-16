# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        

        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.val + 1 == target or node.val - 1 == target:
                    return node.val

                if target < node.val:
                    #go left
                    if node.left:
                        q.append(node.left)
                if target > node.val:
                    #gi rught
                    if node.right:
                        q.append(node.right)
        
        return root.val

            