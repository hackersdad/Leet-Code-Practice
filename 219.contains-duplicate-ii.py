# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = {}
        for i in range(len(nums)):
            if nums[i] in d and abs(i - d[nums[i]]) <= k:
                return True
            d[nums[i]] = i
        
        return False

        
        
        