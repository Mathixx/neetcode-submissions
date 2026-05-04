# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        heap = []
        
        # We need a counter to act as a tie-breaker for identical values
        count = 0 
        
        for node in lists:
            if node: # Important: Only push if the list isn't empty!
                heapq.heappush(heap, (node.val, count, node))
                count += 1
        
        curr = dummy
        while heap:
            # We pop the value and the counter, but we only really need the node
            val, _, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next
            
            # Move to the next node in the specific list we just pulled from
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        return dummy.next
        