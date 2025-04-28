# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

# Example 1:

# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        subsets = []
        m = -1
        c = 0
        
        def find_bitwise_or(arr):
            x = 0
            for i in arr:
                x = x | i
            return x

        def backtrack(index=0,cr=[]):
            nonlocal m,c
            if index == len(nums):
                a = cr[:]
                subsets.append(a)
                current_or = find_bitwise_or(a)
                if current_or == m:
                    c += 1
                elif current_or > m:
                    m = current_or
                    c = 1
                return
            cr.append(nums[index])
            backtrack(index+1,cr)
            cr.pop()
            backtrack(index+1,cr)
        backtrack()
        return c





        