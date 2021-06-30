# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        curr1 = head
        curr2 = head.next
        ans = head.next
        
        while curr1 and curr2:
            temp = curr2.next # stores the next curr1
            curr1.next = curr2.next.next if (curr2.next and curr2.next.next) else curr2.next
            curr2.next = curr1
            
            curr1 = temp
            curr2 = temp.next if curr1 else None
            
        return ans
