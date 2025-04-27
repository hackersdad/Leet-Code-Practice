# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

 

# Example 1:

# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        ans = 0
        subsets = []
        def all_subsets(index,curr_subset):
            if index == len(nums):
                subsets.append(curr_subset[:])
                return
            curr_subset.append(nums[index])
            all_subsets(index+1,curr_subset)
            curr_subset.pop()
            all_subsets(index+1,curr_subset)
        
        all_subsets(0,[])

        for i in subsets:
            print(i)
            temp_xor = 0
            for j in i:
                temp_xor = temp_xor ^ j
            ans += temp_xor
        return ans