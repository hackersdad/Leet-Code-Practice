# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while True and n > 0:
            if n%4 != 0:
                if n == 1:
                    return True
                else:
                    return False
            n = n//4
        return False
        