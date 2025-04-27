# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        t_sum = 0
        t = 0
        while t <len(nums):
            t_sum += nums[t]
            max_sum = max(max_sum,t_sum)
            if t_sum < 0:
                t_sum = 0
            
            t += 1
        return max_sum