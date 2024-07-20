"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        dummy =ListNode(0,head)
        p1 = head
        p2 = head.next
        prev = dummy
        while p1 and p2:
            p1.next = p2.next
            p2.next = p1
            prev.next = p2
            
            # After Swap
            prev = p1
            p1 = p1.next
            if p1:
                p2 = p1.next
            else:
                p2 = None
            
        return dummy.next