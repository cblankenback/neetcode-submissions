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
        
        
        curr = slow.next
        slow.next = None
        left = head

        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        right = prev
            


        while right:
            leftnext = left.next
            rightnext = right.next
            left.next = right
            right.next = leftnext
            left = leftnext
            right = rightnext

