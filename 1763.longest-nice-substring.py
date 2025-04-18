# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def isNice(st):
            big = set()
            small = set()
            for i in st:
                t = ord(i)
                if t < 97:
                    big.add(t)
                else:
                    small.add(t)
            
            for j in big:
                if j+32 in small:
                    small.remove(j + 32)
                else:
                    return False
                
            
            if len(small) == 0:
                return True
            else:
                return False
        
        window_size = len(s)

        while window_size > 1:
            i=0
            while i  <= len(s) - window_size:
                t= s[i:i+window_size]
                if isNice(t):
                    return t
                i += 1

            window_size -= 1
        return ""
                
