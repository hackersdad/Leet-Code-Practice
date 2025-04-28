# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
 

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        d = {0:1}  # Important: prefix 0 seen once initially
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - goal) in d:
                count += d[prefix_sum - goal]
            
            d[prefix_sum] = d.get(prefix_sum, 0) + 1

        return count

        




