# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1 = 0
        p2 = 0
        res = ""
        flag = True
        while p1 < len(word1) and p2 < len(word2):
            if flag:
                res += word1[p1]
                p1 += 1
                flag = False
            else:
                res += word2[p2]
                p2 += 1
                flag = True
        
        while p1< len(word1):
            res += word1[p1]
            p1 += 1
        
        while p2< len(word2):
            res += word2[p2]
            p2 += 1
        return res

            

        