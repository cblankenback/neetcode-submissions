# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None

        curr = right
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head
        right = prev
        while right:
            leftnext = left.next
            rightnext = right.next
            left.next = right
            right.next = leftnext

            left = leftnext
            right = rightnext
        