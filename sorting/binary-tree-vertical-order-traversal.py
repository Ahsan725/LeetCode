class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs 
        if not root:
            return []

        res = []
        col_map = defaultdict(list)
        
        minx = float('inf')
        maxx = float('-inf')
        q = deque([(0, root)])
        
        while q:
            x, node = q.popleft()
            
            col_map[x].append(node.val)
            minx = min(minx, x)
            maxx = max(maxx, x)
            
            if node.left:
                q.append((x - 1, node.left))
            if node.right:
                q.append((x + 1, node.right))
            
        for level in range(minx, maxx + 1):
            res.append(col_map[level])
        return res 
            