"""

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]  

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1h = ListNode(0)
        dummy1 = d1h
        d2h = ListNode(0)
        dummy2 = d2h
        temp = head
        while temp:
            if temp.val < x:
                dummy1.next = ListNode(temp.val)
                dummy1 = dummy1.next
            
            else:
                dummy2.next = ListNode(temp.val)
                dummy2 = dummy2.next
            
            temp = temp.next

        dummy1.next = d2h.next

        return d1h.next
            