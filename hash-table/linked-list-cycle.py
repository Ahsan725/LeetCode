# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # #there is a a two ptr approach as well where one pointer is fast and the other is slow.
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     else:
        #         seen.add(head)
        #     head = head.next
        # return False 

        if not head:
            return None 

        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False
        