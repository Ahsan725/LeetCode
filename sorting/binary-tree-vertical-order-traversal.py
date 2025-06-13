class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #will use bfs 
        #x cordinate method 
        if not root:
            return []
        res = []
        col_map = defaultdict(list)
        q = deque([(0, root)])
        
        while q:
            x, node = q.popleft()
            col_map[x].append(node.val)
            
            
            #add the children
            if node.left:
                q.append((x - 1, node.left))
            if node.right:
                q.append((x + 1, node.right))
                
        #popping elemnts in the right roder in the result 
        sorted_items = sorted(col_map.items())
        for col, val in sorted_items:
            res.append(col_map[col])
        return res
            
            
            
            
        