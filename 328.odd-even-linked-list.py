"""

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Min 3 nodes required to do even something
        if not head or not head.next or not head.next.next:
            return head
        even_head = head.next

        even_pointer = even_head
        odd_pointer = head
        while even_pointer and odd_pointer:
            odd_pointer.next = even_pointer.next
            even_pointer.next = odd_pointer.next.next if odd_pointer.next else None

            even_pointer = even_pointer.next
            
            if odd_pointer.next is None:
                odd_pointer.next = even_head
            elif even_pointer is None and odd_pointer.next.next is None:
                odd_pointer.next.next = even_head
            else:
                odd_pointer = odd_pointer.next

        return head

        
            