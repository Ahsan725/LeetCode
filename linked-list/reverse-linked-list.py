# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #read the current node
        #make a copy node of current node and make its next point to none
        #read the second node and make a copy and make it second point to prev

        prev_node_copied = None

        while head:
            current_org = head #5
            new_node = ListNode(current_org.val) #new_node(5)
            new_node.next = prev_node_copied #prev_node(4) 5->4->3->2->1->None
            prev_node_copied = new_node #5
            head = head.next
        return prev_node_copied
        