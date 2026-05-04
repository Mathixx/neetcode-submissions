# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for k, node in enumerate(lists):
            heapq.heappush(heap, (node.val,k))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            _, idx = heapq.heappop(heap)
            curr.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            curr=curr.next
        
        return dummy.next
