# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.


class Solution:
    def addDigits(self, num: int) -> int:
        def sumdigits(n):
            s = 0
            while n > 0:
                s += n%10
                n = n//10
            return s
        num = sumdigits(num)
        while num >= 10:
            num = sumdigits(num)
        return num
        