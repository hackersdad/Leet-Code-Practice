# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.
 

# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        # ans =0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         t = nums[i] - nums[j] if nums[i] > nums[j] else nums[j] - nums[i]
        #         if t == k:
        #             ans += 1
        # return ans

        d = {}
        for i in nums:
            if i in d:
                t = d[i]
                d[i] = t + 1
            else:
                d[i] = 1
        ans = 0
        for j in nums:
            p = j - k
            q = j + k
            if p in d:
                ans += d[p]
            if p != q and q in d:
                ans += d[q]
        return ans//2  


        