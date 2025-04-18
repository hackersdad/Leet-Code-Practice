"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        n  = 0
        while temp:
            temp = temp.next
            n += 1

        if k >= n:
            base_size = 1
            bigger_list_count = 0
        else:
            base_size = n//k
            bigger_list_count = n%k

        k_counter = 1
        temp = head
        res = []
        while k_counter <= k:
            temp_list_head = temp
            res.append(temp_list_head)
            sub_counter = 0 if bigger_list_count > 0 else 1
            if bigger_list_count > 0 :
                bigger_list_count -= 1
            while sub_counter < base_size and temp:
                temp = temp.next
                sub_counter += 1
            
            if temp:
                new_temp = temp.next
                temp.next = None
                temp = new_temp                  

            k_counter += 1

        return res


