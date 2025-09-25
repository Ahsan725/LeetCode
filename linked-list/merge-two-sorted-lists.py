# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #why do we need a dummy? because I am creating a NEW sorted list and that means I will have to insert a new node
        dummy = ListNode()
        cur = dummy 
        
        #I had l2.val before because I was trying to access the valye but I need the node not the valye
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            #update the cur ptr
            cur = cur.next
            
        cur.next = l1 or l2
        
        return dummy.next
