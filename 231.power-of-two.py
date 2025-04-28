# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        while True and n > 0:
            if n%2 != 0:
                if n == 1:
                    return True
                else:
                    return False
            n = n//2
        return False
                

        