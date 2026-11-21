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
        curr = head
        left = head
        right = prev
        # take each one
        while left and right:
            nextright = right.next
            nextleft = left.next
            curr.next = right
            curr.next.next = nextleft
            curr = curr.next.next
            right = nextright
            left = nextleft
        



