class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False
         
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))  

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))


    """
    The function isSubtree first checks if t is empty. If t is empty, it immediately returns True because an empty tree is considered a subtree of any tree. If s is empty but t is not, it returns False because a non-empty tree cannot be a subtree of an empty tree. Next, the function checks if the current nodes of s and t are identical by calling the helper function sameTree. If they are the same, it returns True. Otherwise, it recursively checks the left and right subtrees of s to see if t is a subtree of either. The helper function sameTree compares two trees, s and t, to see if they are structurally identical. It does so by checking the values of the current nodes and recursively ensuring that both the left and right subtrees match. If both trees are empty at any point, it returns True, indicating they are identical at that point. If one tree is empty while the other is not, or their values do not match, it returns False.
    """