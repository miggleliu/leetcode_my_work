# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        # Compare one by one
        # result = lists[0]
        # for i in range(len(lists) - 1):
        #     result = self.merge2Lists(result, lists[i+1])
        
        # Compare by divide and conquer
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]
            
        
    def merge2Lists(self, l1 : List[ListNode], l2 : List[ListNode]) -> ListNode:
        result = ListNode(0)
        curr = result
        curr1 = l1
        curr2 = l2
        
        while curr1 is not None and curr2 is not None:
            if curr1.val > curr2.val:
                curr.next = curr2
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr1 = curr1.next
            curr = curr.next
        
        if curr2:
            curr.next = curr2
        elif curr1:
            curr.next = curr1
        
        return result.next
            
        
