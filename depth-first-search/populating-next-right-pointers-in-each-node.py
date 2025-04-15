"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #some common things about all BFS solutions 
        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q) #we save this because len of q will change but we need a snapshot of size
            for i in range(size):
                node = q.popleft()
 
                if i < size - 1: #this is why we needed the size and why len(q) would not work by itself.
                    node.next = q[0]
                
                #appending the children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return root
