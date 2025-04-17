# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # d = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        # for c in sentence:
        #     d[c] = d.get(c,0) + 1
        # for x in d:
        #     if d[x] == 0:
        #         return False
        # return True

        z =  ord('z')
        a = ord('a') - 1
        s = int(((z-a)*(z+a+1))/2)
        new_s = set(sentence)
        ts = 0
        for i in new_s:
            ts += ord(i)
        if ts != s:
            return False
        return True

        