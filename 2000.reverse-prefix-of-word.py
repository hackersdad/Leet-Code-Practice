# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

 

# Example 1:

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        flag = False
        for i in range(len(word)):
            if word[i] == ch:
                flag = True
                break
        if flag:
            t = word[0:i+1]
            res = t[::-1] + word[i+1:]
            return res
        else:
            return word

        