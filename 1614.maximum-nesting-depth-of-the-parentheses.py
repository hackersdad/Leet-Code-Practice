# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        i = 0
        m = 0
        l = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
                l += 1
                m = max(l,m)
            if s[i] == ")":
                stack.pop()
                l -= 1
            i += 1
        return m


        