# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestVa# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        c = root.val
        while root:
            # update the closest value once the current note's value is more closet to target:
            if abs(root.val - target) < abs(c - target):
                c = root.val
            # use the binary search tree's property to find the closest value to target
            else:
                if root.val < target:
                    root = root.right
                else:
                    root = root.left
        return calue(self, root: Optional[TreeNode], target: float) -> int:
        

        q = deque([root])
        closest = root.val

        while q:
            node = q.popleft()

            if abs(node.val - target) < abs(closest - target):
                closest = node.val

            if target < node.val:
                #go left
                if node.left:
                    q.append(node.left)
            if target > node.val:
                #gi rught
                if node.right:
                    q.append(node.right)
        
        return closest

            