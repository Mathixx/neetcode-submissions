# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        curr = dummy.next
        first = curr
        prev_group = dummy
        count = 1
        while curr:
            if count == k:
                # reverse list
                next_group = curr.next

                prev = next_group
                curr_reverse = first
                for i in range(k):
                    temp = curr_reverse.next
                    curr_reverse.next = prev
                    prev = curr_reverse

                    curr_reverse = temp
                
                prev_group.next = prev
                prev_group = first
                    
                count = 1
                first = next_group
                curr = next_group
            else:
                curr = curr.next
                count += 1
        
        return dummy.next

        