# You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

# Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

 

# Example 1:


# Input: head = [0,1,2,3], nums = [0,1,3]
# Output: 2
# Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        c = 0
        s = set(nums)
        temp = head
        while temp:
            if temp.val in s:
                c += 1
                while temp and temp.val in s:
                    s.remove(temp.val)
                    temp = temp.next
            else:
                temp = temp.next
        return  c

        