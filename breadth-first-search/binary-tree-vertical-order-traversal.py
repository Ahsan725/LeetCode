class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #will use bfs 
        #x cordinate method 
        if not root:
            return []
        res = []
        minx = float('inf')
        maxx = float('-inf')
        col_map = defaultdict(list)
        q = deque([(0, root)])
        
        while q:
            x, node = q.popleft()
            col_map[x].append(node.val)
            minx = min(minx, x)
            maxx = max(maxx, x)
            
            #add the children
            if node.left:
                q.append((x - 1, node.left))
            if node.right:
                q.append((x + 1, node.right))
                
        #popping elemnts in the right roder in the result 
        # sorted_items = sorted(col_map.items())
        # for col, val in sorted_items:
        #     res.append(col_map[col])
        # return res

        for i in range(minx, maxx + 1):
            res.append(col_map[i])
        return res
            
        #Time: O(nlogn) -> this from sorting
        #Space: O(n)
            
            
            
        