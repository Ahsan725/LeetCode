class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #idea of the algo is that root we consider (0,0) cordinate if we go left a col thats -1 if we go right + 1

        """
        Approach:
        - Use BFS to traverse the tree while tracking horizontal distances (x-coordinates).
        - Use a hashmap (col_map) to group node values by their column index.
        - Keep track of min and max x to build the result in left-to-right column order.
        """
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
            