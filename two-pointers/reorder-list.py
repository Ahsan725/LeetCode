# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Step 1: Find the midpoint of the linked list

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #slow will have the mid point for our linkedlist 

        #Step 2: Reverse the second half of the linkedlist 
        prev = None
        cur = slow
        while cur:
            cur.next, prev, cur  = prev, cur, cur.next

        #Step 3: Merge the two linked lists
        first = head
        second = prev

        while second.next:
            #1->2->3
            #6->5->4
            first.next, first = second, first.next
            second.next, second = first, second.next