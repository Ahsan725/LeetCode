# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #BFS Solution
        # q = deque([root])
        # level = 0
        
        # while q:
        #     for _ in range(len(q)):
        #         current = q.popleft()
        #         if current.left:
        #             q.append(current.left)
        #         if current.right:
        #             q.append(current.right)
        #     level += 1

        # return level 
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res