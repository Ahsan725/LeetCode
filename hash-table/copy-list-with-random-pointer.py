"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #basically we are copying the linkedlist in a way that all the connections translate over to the new linked list
        #has two pointers next and random 
        #iterate over each node and get two values
        if not head: return None
        
        oldtonew = {None : None}

        cur = head
        while cur:
            newnode = Node(cur.val)
            oldtonew[cur] = newnode
            cur = cur.next

        cur = head #{old : new}
        while cur:
            newnode = oldtonew[cur]
            newnode.next = oldtonew[cur.next]
            newnode.random = oldtonew[cur.random]
            cur = cur.next

        return oldtonew[head]
