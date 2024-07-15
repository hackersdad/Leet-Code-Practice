"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        l1_current = l1
        l2_current = l2
        head = ListNode(0) 
        new_current = head
        while l1_current or l2_current or carry > 0:
            
            n1 = l1_current.val if l1_current else 0
            n2 = l2_current.val if l2_current else 0
            
            s = n1+n2+carry
            if s > 9 :
                carry = int(str(s)[0])
                node_val = int(str(s)[1])
            else:
                carry = 0
                node_val = s
            
            new_current.next = ListNode(node_val)
            new_current = new_current.next
            if(l1_current):
                l1_current=l1_current.next
            if(l2_current):
                l2_current=l2_current.next
        
        return head.next
