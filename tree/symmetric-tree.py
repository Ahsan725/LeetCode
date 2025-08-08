class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        #understanding: we are checking if the tree when split in half right down the middle if it is mirror image of its one side. 
        #approach: use bfs using a q and go level by level collect all the values and then compare them against their reverse
        
        #base case
        if not root:
            return root
        q = deque([root])
        
        while q:
            level_len = len(q)
            level_vals = []
            
            for _ in range(level_len):
                node = q.popleft()
                if node:
                    level_vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level_vals.append(None)

            if level_vals != level_vals[::-1]:
                return False 
        return True