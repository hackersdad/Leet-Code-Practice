# You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

# Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
# Remove the last element from the current array nums.
# Return an array answer, where answer[i] is the answer to the ith query.

 

# Example 1:

# Input: nums = [0,1,1,3], maximumBit = 2
# Output: [0,3,2,3]
# Explanation: The queries are answered as follows:
# 1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
# 2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
# 3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
# 4th query: nums = [0], k = 3 since 0 XOR 3 = 3.

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        ans=[]
        temp = 2**maximumBit - 1
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] ^ nums[i]
            ans.append(nums[i] ^ temp)
        ans.insert(0,nums[0]^temp)
        return ans[::-1]    
        