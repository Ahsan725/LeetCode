# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0 
        dummy = ListNode()
        cur = dummy
        
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            total = num1 + num2 + carry
            carry = total // 10
            val = total % 10
            cur.next = ListNode(val)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        
        return dummy.next
        