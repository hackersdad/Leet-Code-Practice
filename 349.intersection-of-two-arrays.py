# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = set(nums1)
        n2 = set(nums2)

        t_small = n1 if len(n1) <= len(n2) else n2
        t_big = n1 if len(n1) > len(n2) else n2

        ans = set()
        for i in t_small:
            if i in t_big:
                ans.add(i)
        return list(ans)