"""

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        int_to_freq = {}
        for i in nums:
            if i in int_to_freq:
                int_to_freq[i] += 1
            else:
                int_to_freq[i] = 1
                
        freq_to_int = {}
        for key in int_to_freq:
            if int_to_freq[key] in freq_to_int:
                temp = freq_to_int[int_to_freq[key]]
                t_l = len(temp)
                k = 0
                while k < t_l:
                    if int(key) > temp[k]:
                        break
                    k += 1
                temp.insert(k,key)
                freq_to_int[int_to_freq[key]] = temp
            else:
                freq_to_int[int_to_freq[key]] = [key]
        
        freq_arr = list(freq_to_int.keys())
        freq_arr.sort()
        res = []
        for i in freq_arr:
            for j in freq_to_int[i]:
                res.extend([j]*i)
        return res