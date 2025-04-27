# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        a = []
        for i in d:
            a.append((d[i],i))
        a.sort(reverse = True)

        ans = []
        for j in range(k):
            ans += [a[j][1]]
        return ans



        