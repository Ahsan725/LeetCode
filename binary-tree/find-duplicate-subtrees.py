# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        #create a string representation of the tree which can be used as a hashable key in the hashmap
        #
        def dfs(node):
            if not node:
                return "#" #could be anything like null
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subtrees[s]) == 1: #if there was already a tree like this in the list of the hashmap with key s. 
            #we also only want to add it once in the res that's why it is set to == 1 
                res.append(node) #we found a duplicate so add to the res
            subtrees[s].append(node) #reagrdless we should add it to the hashmap 
            return s

        res = []
        dfs(root)
        return res