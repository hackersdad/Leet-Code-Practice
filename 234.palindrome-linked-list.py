"""

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        prev= None
        temp = head
        while temp:
            prev = ListNode(temp.val, prev)
            temp = temp.next
        
        temp = head
        rev_temp = prev
        while temp:
            if temp.val != rev_temp.val:
                return False
            temp = temp.next
            rev_temp = rev_temp.next
        return True
        