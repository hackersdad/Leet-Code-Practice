# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".

class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        i=0
        c=0
        while i  < len(s) - 2:
            t= s[i:i+3]
            if len(t) == len(set(t)):
                c += 1
            
            i += 1
        return c