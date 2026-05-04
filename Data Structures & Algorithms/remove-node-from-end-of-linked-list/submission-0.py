# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        k = size - n
        curr = head
        dummy = ListNode(0, head)
        prev = dummy
        while k:
            prev, curr = curr, curr.next
            k-=1
        
        prev.next = curr.next
        return dummy.next



        