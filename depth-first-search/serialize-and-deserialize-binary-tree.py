# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder_dfs(root):

            #base case
            if not root:
                res.append("#")
            
            #appending the value 
            res.append(str(root.val))

            #left sub tree
            preorder_dfs(root.left)
            #right sub tree
            preorder_dfs(root.right)

        preorder_dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.idx = 0

        def build(values)
        #base case
        if values[self.idx] == "#":
            self.idx += 1
            return None
        
        #append the value
        node = TreeNode(int(values[self.idx)])
        self.idx += 1
        
        #left sub tree
        build(node.left)
        #right sub tree
        build(node.right)
        return node

    

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))