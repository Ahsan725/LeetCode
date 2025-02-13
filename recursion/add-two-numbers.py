# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy 
        
        carry = 0
        while l1 or l2 or carry:
            #extract the values to add
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            #calculate the sum and carry and the value to add
            total = num1 + num2 + carry
            carry = total // 10
            value = total % 10
            #create a new listnode and add the value
            cur.next = ListNode(value)
            #move all the three of the linked list pointers 
            cur = cur.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            
        return dummy.next
        
