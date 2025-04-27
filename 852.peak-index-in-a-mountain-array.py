# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]

# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]

# Output: 1

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # prev = 0
        # i = 1
        # while i < len(arr):
        #     if arr[prev] > arr[i]:
        #         return prev
        #     prev = i
        #     i += 1
        # return i

        l = 0
        h = len(arr) - 1

        while l <= h:
            mid = (l+h)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            
            if arr[mid] < arr[mid+1]:
                l=mid+1
            if arr[mid] > arr[mid+1]:
                h=mid-1
        
        return l





        
        