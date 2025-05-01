# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        v = set(['a','e','i','o','u'])
        vc = 0 
        for i in s[:k]:
            if i in v:
               vc += 1
        
        l=0
        sub = s[0:k]
        temp_count = vc
        while l < len(s) - k:
            out = s[l]
            inn = s[l+k]
            if out in v:
                temp_count -= 1
            if inn in v:
                temp_count += 1
            vc = max(vc,temp_count)
            l += 1
        return vc

                


        