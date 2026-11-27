# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + remainder
            # how many 10s are there in 15
            remainder = total // 10
            # what is the remainder if we devide by 10(ei remove all the 10s)
            total = total % 10
            curr.next = ListNode(total)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        curr.next = ListNode(remainder) if remainder != 0 else None
        return dummy.next
