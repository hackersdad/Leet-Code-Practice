# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        d = {}
        n = len(nums)
        for i in nums:
            d[i] = d.get(i,0) + 1
            if d[i] > n//2:
                return i
        
        

        