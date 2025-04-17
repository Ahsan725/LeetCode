# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_map = defaultdict(list)
        min_col = float('inf')
        max_col = float('-inf')
        res = []
        
        q = deque([(root, 0, 0)])
        while q:
            node, row, col =  q.popleft()
            col_map[col].append((row, node.val))
            
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        
        for level in range(min_col, max_col + 1):
            items = col_map[level]
            items.sort()
            
            res.append([val for _, val in items]) #we wont use the row could be replaced with _,
        return res
                        
        