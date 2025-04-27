# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation: 
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6
# Example 2:

# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        # flag = 0
        # p1 = int(k//2)
        # if k%2 == 0:
        #     flag = 1
        # ans = []
        # for i in range(len(nums)-k+1):
        #     temp = nums[i:i+k]
        #     temp.sort()
        #     if flag == 0:
        #         t = temp[p1]
        #     else:
        #         t = (temp[p1] + temp[p1-1])/2
        #     ans.append(t)
        # return ans

        def bisect_left(arr, x):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low


        def insert(arr, x):
            idx = bisect_left(arr, x)
            arr.insert(idx, x)
            return arr


        def remove(arr, x):
            idx = bisect_left(arr, x)
            if idx < len(arr) and arr[idx] == x:
                arr.pop(idx)
            return arr


        flag = 0
        p1 = int(k // 2)
        if k % 2 == 0:
            flag = 1

        def med(arr):
            if flag == 0:
                return arr[p1]
            else:
                return (arr[p1] + arr[p1 - 1]) / 2

        ans = []
        carry = sorted(nums[:k])
        ans.append(med(carry))

        for i in range(k, len(nums)):
            carry = remove(carry, nums[i - k])
            carry = insert(carry, nums[i])
            ans.append(med(carry))

        return ans





        