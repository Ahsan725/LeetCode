# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        #you are basically taking the current node and changing its value to the value of its next node
        #then you make this current node point to the next of the next node
        #essentially you are not deleting this node you are making this node a copy of the next node
        #and removing the pointer to next node thus essentially deleting it
    

        cur_node = node
        cur_node.val = cur_node.next.val
        cur_node.next = cur_node.next.next

