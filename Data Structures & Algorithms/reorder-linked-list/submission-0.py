# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into second and first
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse
        second = slow.next
        slow.next = None
        first = head

        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second = prev


        # insert
        # first  2 > 4 > None
        # second 8 > 6 > None
        # first  2 > 8 > 6 > None
        while second:
            tmp1 = first.next
            first.next = second
            tmp2 = second
            second = second.next
            first = tmp1
            tmp2.next = tmp1
            first = tmp2.next





        