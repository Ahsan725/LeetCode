# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #understanding: use a dummy node, iterate over it and swap first and second by reiwiring next 
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            tail = second.next

            prev.next = second
            second.next = first
            first.next = tail

            prev = first

        return dummy.next

        