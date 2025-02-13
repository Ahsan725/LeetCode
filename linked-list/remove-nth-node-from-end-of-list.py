from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # Move `fast` n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow, fast = slow.next, fast.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next

        """
        This is a double-pass solution that may be easier to come up with in an interview.
        
        class Solution:
            def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                # First pass: Compute the length of the list
                length = 0
                temp = head
                while temp:
                    length += 1
                    temp = temp.next
                
                # Find the position to remove (0-based index)
                remove_pos = length - n

                # Edge case: If we need to remove the first node
                if remove_pos == 0:
                    return head.next

                # Second pass: Traverse again to remove the node
                dummy = ListNode(0, head)
                temp = dummy
                for _ in range(remove_pos):
                    temp = temp.next

                # Remove the target node
                temp.next = temp.next.next

                return dummy.next
        """
