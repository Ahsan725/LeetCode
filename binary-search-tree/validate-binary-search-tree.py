# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node: #base condition 1
                return True
            if not (low < node.val < high): #base condition 2
                return False
                
#if going left we do not know how small the value of the node will be so we use the low (-inf) but we know which value it NEEDS to be bigger than which is its parents right bount aka node.val. This is the same for the right node we dont the upper bound but we do know lower bound aka node.val 

            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)

# class Solution:
#bfs solution
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         q = deque([(root, float('-inf'), float('inf'))])
#         while q:
#             node, low, high = q.popleft()
#             if not (low < node.val < high):
#                 return False

#             if node.left:
#                 q.append((node.left, low, node.val))
#             if node.right:
#                 q.append((node.right, node.val, high))
#         return True

