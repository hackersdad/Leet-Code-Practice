# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            d[t[i]] = d.get(t[i],0) - 1
        
        for j in d:
            if d[j] != 0:
                return False
        return True
