# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

 

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        d = {}
        for i in range(len(arr)):
            d[arr[i]] = d.get(arr[i],0) + 1
        
        r = []
        for j in d:
            if d[j] == 1:
                r.append(j)
        if len(r) < k:
            return ""
        else:
            return r[k-1]
        