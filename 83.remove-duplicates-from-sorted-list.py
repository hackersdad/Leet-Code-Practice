"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next

        return dummy.next