# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = l1
        l2curr = l2
        remainder = 0
        head = ListNode()
        res = head
        while l1curr or l2curr or remainder:
            v1 = l1curr.val if l1curr else 0
            v2 = l2curr.val if l2curr else 0
            total = v1 + v2 + remainder
            remainder = 0
            while total > 9:
                remainder += 1
                total -= 10
            
            
            
            res.next = ListNode(total)
            total = 0
            res = res.next
            l1curr = l1curr.next if l1curr else None
            l2curr = l2curr.next if l2curr else None
        return head.next