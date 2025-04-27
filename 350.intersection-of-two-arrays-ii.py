# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = {}
        d2 = {}
        for i in nums1:
            d[i] = d.get(i,0) + 1
        
        for i in nums2:
            d2[i] = d2.get(i,0) + 1
        
        ans = []

        a = set(nums2)
        for j in d:
            if j in a:
                ans +=  [j]* min(d[j],d2[j])
        return ans
        