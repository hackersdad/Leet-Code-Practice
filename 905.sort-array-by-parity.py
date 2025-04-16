# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        def even(n):
            return n%2 == 0
        def odd(n):
            return n%2 != 0
        left, right = 0, len(nums) - 1

        while left < right:
            if odd(nums[left]) and even(nums[right]):
                nums[left], nums[right] = nums[right], nums[left]
            
            if even(nums[left]):
                left += 1
            if odd(nums[right]):
                right -= 1

        return nums
        