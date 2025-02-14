# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #heap 
        heap = []
        #this only loads the heads of the lists on the heap so we can look at one item at a time from all(k) lists
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
            
        dummy = ListNode()
        cur = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            #I had a confusion here the i is not the index of the next node rather the index of the list in the main
            #list e.g list#1, list#2 and so on which is why you do not need to update the i when pushing
            if node:
                heapq.heappush(heap, (node.val, i, node))
        return dummy.next
        