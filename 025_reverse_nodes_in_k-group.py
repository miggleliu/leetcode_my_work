# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        
        # find the length and the new head
        length = 0
        explorer = head
        while explorer:
            length += 1
            if length == k:
                new_head = explorer
            explorer = explorer.next
        
        num_of_block = length // k
        
        # curr1 and curr2 are responsible for swapping the adjacent nodes
        # curr_block_last and next_block_first are responsible for connecting the adjacent blocks
        curr1 = curr_block_last = head
        curr2 = head.next
        next_block_first = new_head
        
        
        for i in range(num_of_block):
            
            # update next_block_first to be the first node of the next block
            for j in range(k):
                if next_block_first:
                    next_block_first = next_block_first.next
                else:
                    break
                
            for j in range(k - 1):
                # swap curr1 and curr2
                temp = curr2.next
                curr2.next = curr1
                curr1 = curr2
                curr2 = temp
            
            # build connections
            if next_block_first:
                curr_block_last.next = next_block_first
                curr_block_last = curr2
                curr1 = curr2
                curr2 = curr2.next
            else:
                curr_block_last.next = curr2
           
        
        return new_head
        
