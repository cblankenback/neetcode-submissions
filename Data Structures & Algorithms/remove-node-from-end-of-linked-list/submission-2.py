# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1,2,3,4,5,6,8,9,10 n= 5
        #   l         r

        # 1,2,3,4
        #   l   r
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for i in range(n):
            right = right.next
        

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next



