class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root):
        """Encodes an N-ary tree to a single string using preorder traversal."""
        serial = []

        def dfs(node):
            if not node:
                return
            # Append the value and number of children
            serial.append(str(node.val))
            serial.append(str(len(node.children)))
            for child in node.children:
                dfs(child)

        dfs(root)
        return ' '.join(serial)

    def deserialize(self, data):
        """Decodes the serialized string back to an N-ary tree."""
        if not data:
            return None

        tokens = data.split()
        self.index = 0

        def dfs():
            val = int(tokens[self.index])
            self.index += 1
            num_children = int(tokens[self.index])
            self.index += 1
            node = Node(val)
            for _ in range(num_children):
                node.children.append(dfs())
            return node

        return dfs()
