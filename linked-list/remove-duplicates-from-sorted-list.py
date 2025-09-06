# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        cur = dummy
        last_node = ListNode()

        while cur and last_node:
            if cur.val == last_node.val:
                last_node.next = last_node.next.next
                cur = last_node
            
            last_node = cur
            cur = cur.next
        
        return head