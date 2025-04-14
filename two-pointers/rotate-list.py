# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        #[to solve this problem we need 4 variables: new tail, new head, org_head, org_tail
        #then we do this new_tail -> None, org_tail -> org_head, return new_head
        #this is the entire solution rest is basically how do we find these node positions]

        # Step 1: Compute the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k (in case it's >= length) (e.g k = 17 this is the same as rotating by 2 if len is 5)
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the new tail node (at index length - k - 1)
        #new tail is basically the node where we will cut the list
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: Set the new head and reconnect the links
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head

        