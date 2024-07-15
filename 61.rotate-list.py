"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        # Find the length and connect the list to form a cycle
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head

        # Find the new head
        skip = n - k % n  # Calculate the number of nodes to skip
        new_tail = head
        for _ in range(skip - 1):
            new_tail = new_tail.next
        head = new_tail.next
        new_tail.next = None

        return head   