# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode()
        curr_sum = sum
        curr1 = l1
        curr2 = l2
        carry = 0
        
        while curr1 or curr2:
            
            # fill in zeros if two numbers are of different lengths
            if not curr1:
                curr1 = ListNode()
            elif not curr2:
                curr2 = ListNode()
                
            # calculate every digit and carry correspondingly
            digit = (curr1.val + curr2.val + carry) % 10
            carry = (curr1.val + curr2.val + carry) // 10
            curr_sum.next = ListNode(digit, None)
            
            curr1 = curr1.next
            curr2 = curr2.next
            curr_sum = curr_sum.next
            
        if carry == 1:
            curr_sum.next = ListNode(1)
        
        return sum.next
