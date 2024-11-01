# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case: if the node is None, return 0
        if not root:
            return 0

        # Case 1: Node's value is within the range
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        # Case 2: Node's value is less than the range's lower bound
        elif root.val < low:
            # Only search the right subtree because left subtree values will be too small
            return self.rangeSumBST(root.right, low, high)

        # Case 3: Node's value is greater than the range's upper bound
        else:  # root.val > high
            # Only search the left subtree because right subtree values will be too large
            return self.rangeSumBST(root.left, low, high)
