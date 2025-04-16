# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                temp = d[nums[i]]
                temp.append(i)
                d[nums[i]] = temp
            else:
                d[nums[i]] = [i]
        ans = 0
        for j in d:
            t = len(d[j])
            ans += (t * (t-1))/2
        return int(ans)
