# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        remove = count - n
        count = 0
        curr = head
        dummy = ListNode(0, head)
        prev = dummy
        while remove > count:
            count += 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return dummy.next



        