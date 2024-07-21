"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        prev = dummy
        current = head
        while current and current.next:
            node_val = current.val
            next_val = current.next.val
            if  node_val == next_val:
                temp_current = current.next
                while node_val == next_val and temp_current:
                    temp_current = temp_current.next
                    next_val = temp_current.val if temp_current else None
                prev.next = temp_current
                current = temp_current
            else:
                prev = prev.next
            
                current = current.next if current else None
        return dummy.next
        

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Create a dummy node that points to the head of the list
#         dummy = ListNode(0, head)
#         prev = dummy  # This will be the last node in the new list without duplicates
#         current = head  # This will be used to traverse the original list
        
#         while current:
#             # Check if current node has a duplicate
#             if current.next and current.val == current.next.val:
#                 # Skip all nodes with the same value
#                 while current.next and current.val == current.next.val:
#                     current = current.next
#                 # Link prev node to the node after the last duplicate
#                 prev.next = current.next
#             else:
#                 # If no duplicate, just move prev
#                 prev = prev.next
#             # Move current to the next node
#             current = current.next
        
#         return dummy.next