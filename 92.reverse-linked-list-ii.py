"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        dummy = ListNode(0,head)
        prev_to_left = dummy
        left_tracker = 1
        temp = head
        while left_tracker < left:
            prev_to_left = temp
            temp = temp.next
            left_tracker += 1
        
        left_starting = prev_to_left.next 
        
        right_tracker = 1
        rev_prev = None
        rev_temp = left_starting
        while right_tracker <= right-left + 1:
            new_temp = rev_temp.next
            rev_temp.next = rev_prev
            rev_prev = rev_temp
            rev_temp = new_temp
            right_tracker += 1
        
        left_starting.next = new_temp
        prev_to_left.next = rev_prev
        
        return dummy.next
        
        