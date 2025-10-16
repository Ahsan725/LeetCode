# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = ListNode()
        dummy = ListNode()
        dummy.next = head #in case we have to delete the head
        cur = head
        prev = dummy
        while cur:
            if cur and cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
            

        return dummy.next
