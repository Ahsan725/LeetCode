# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #approach: iterate over the array and save the two values by adding them reverse them at the end

        number = 0
        number2 = 0
        while l1:
            number = (number * 10) + l1.val
            l1 = l1.next
        

        while l2:
            number2 = (number2 + 10) + l2.val
            l2 = l2.next

        sum_of_nums = number + number2 #708
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #approach: iterate over the array and save the two values by adding them reverse them at the end

        number = 0
        number2 = 0
        while l1:
            number = (number * 10) + l1.val
            l1 = l1.next
        num1_string = str(number)
        reverse_nums1 = num1_string[::-1]
        reverse_nums1 = int(reverse_nums1)
            

        while l2:
            number2 = (number2 * 10) + l2.val
            l2 = l2.next
        num2_string = str(number2)
        reverse_nums2 = num2_string[::-1]
        reverse_nums2 = int(reverse_nums2)

        sum_of_nums = str(reverse_nums1 + reverse_nums2 )#196
        reversed_sum = sum_of_nums[::-1] #691
    
        #98 + 98 = 196 -> 8->9 8->9  === 89 then we reversed it so it became 98 + 98 -> 196 but we need ll -> 691
        #243 564 -> 342 + 465 = 807 -> 708 
        dummy_head = ListNode(0)
        current = dummy_head
        for digit in reversed_sum:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy_head.next

    
