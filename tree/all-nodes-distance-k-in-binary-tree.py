class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == k:
                res.append(node.val)
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # Start DFS from target node
        dfs(target, 0)
        return res
