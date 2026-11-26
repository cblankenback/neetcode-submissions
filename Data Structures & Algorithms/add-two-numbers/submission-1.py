# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        remainder = 0
        while l1 or l2:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0
            num = l1_num + l2_num + remainder
            remainder = 0
            
            remainder = num // 10
            num = num % 10
            
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remainder != 0:
            curr.next = ListNode(remainder)
        return dummy.next
