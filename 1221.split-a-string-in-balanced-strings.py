# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

class Solution:
    def balancedStringSplit(self, s: str) -> int:

        count = 0
        f=0
        for i in s:
            if i =="R":
                f += 1
            else:
                f -= 1
            if f==0:
                count += 1
        return count




        