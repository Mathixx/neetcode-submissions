# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add2(l1, l2, reminder=False):
            if not l1 and not l2:
                if reminder:
                    return ListNode(1)
                return None            
            
            value = 1 if reminder else 0
            if l1:
                value += l1.val
            if l2:
                value+= l2.val

            new_node = ListNode(value%10)
            new_node.next = add2(l1.next if l1 else None, l2.next if l2 else None, reminder=(value>9))
            return new_node
        
        return add2(l1, l2, reminder=False)
            

        