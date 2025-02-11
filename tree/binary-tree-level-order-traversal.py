class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            level_size = len(q)  # Number of nodes at the current level this so we can run the loop this many times
            level_nodes = []  # Stores node values for this level since we are returning a list of lists

            for _ in range(level_size):
                current = q.popleft()
                level_nodes.append(current.val)  # Store value, not node
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            
            res.append(level_nodes)  # Append the entire level to result
        
        return res
