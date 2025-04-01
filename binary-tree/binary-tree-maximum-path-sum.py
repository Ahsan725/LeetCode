# Definition for a binary tree node in Python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # We'll store the overall maximum path sum here
        self.globalMaxSum = float('-inf')
        
        def maxPathSumHelper(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Recursively get max path sum from left and right children
            left = maxPathSumHelper(node.left)
            right = maxPathSumHelper(node.right)
            
            # Possible ways to form a path through this node:
            link2neither = node.val                  # just the node itself
            link2left = node.val + left             # node + left path
            link2right = node.val + right           # node + right path
            link2both = node.val + left + right     # node + left + right (fully passing through this node)
            
            # For continuing upward, we can only link this node alone,
            # or this node with either left or right (but not both).
            linkableMaxSum = max(link2neither, link2left, link2right)
            
            # Update the global maximum path sum if needed
            # (the path can include both children at once for the global sum)
            self.globalMaxSum = max(self.globalMaxSum, link2both, linkableMaxSum)
            
            # Return the best sum that can be "continued" upwards to the parent
            return linkableMaxSum
        
        maxPathSumHelper(root)
        return self.globalMaxSum
