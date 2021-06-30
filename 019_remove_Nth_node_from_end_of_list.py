# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        for i in range(n+1):
            second = second.next
        
        while second:
            second = second.next
            first = first.next
            
        if first.next.next:
            first.next = first.next.next
        else:
            first.next = None
        
        return dummy.next
