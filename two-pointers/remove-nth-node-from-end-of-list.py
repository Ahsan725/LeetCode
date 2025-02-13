from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Find length of the list
        length = 0
        temp = head  # Keep a reference to head
        while temp:
            length += 1
            temp = temp.next

        # Step 2: Find position to remove (0-based index)
        remove_pos = length - n
        
        # Edge case: If we need to remove the first node
        if remove_pos == 0:
            return head.next

        # Step 3: Traverse again to remove the node
        temp = head
        for _ in range(remove_pos - 1):
            temp = temp.next
        
        # Step 4: Remove the node
        temp.next = temp.next.next

        return head
