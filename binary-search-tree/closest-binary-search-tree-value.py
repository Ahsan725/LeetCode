class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            if abs(node.val - target) <= abs(closest - target):
                closest = node.val


            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest
