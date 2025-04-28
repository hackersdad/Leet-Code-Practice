# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:

# Input: l1 = [0], l2 = [0]
# Output: [0]
 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head_node):
            prev = None
            temp = head_node 
            while temp:
                t = temp.next
                temp.next = prev
                prev = temp
                temp = t
            return prev
        rl1 = reverse(l1)
        rl2 = reverse(l2)
        
        temp1 = rl1
        temp2 = rl2
        carry = 0
        prev = ListNode(0)
        final = prev
        while temp1 or temp2 or carry > 0:
            s = 0 
            if temp1:
                t1 = temp1.val
                s += t1
                temp1 = temp1.next
            if temp2:
                t2 = temp2.val
                s += t2
                temp2 = temp2.next
            s += carry

            if s > 9:
                p = s%10
                carry = s//10
                s = p
            else:
                carry = 0
            
            node = ListNode(s)
            prev.next = node
            prev = node

        final = reverse(final.next)
        return final
            

        