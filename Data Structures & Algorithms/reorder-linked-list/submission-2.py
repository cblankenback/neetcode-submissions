# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       
        #reverse
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        left = head
        right = prev
        # take each one
        while right:
            leftnext = left.next
            rightnext = right.next
            left.next = right
            right.next = leftnext
            left = leftnext
            right = rightnext
        



