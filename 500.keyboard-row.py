"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        k = ["qwertyuiop", "asdfghjkl", "zxcvbnm" ]
        
        def check_word_can_be_made(inp):
            p = 0
            if inp[0].lower() in k[1]:
                p = 1
            if inp[0].lower() in k[2]:
                p = 2
                        
            for i in inp:
                if i.lower() not in k[p]:
                    return False
            return True 

        return [w for w in words if check_word_can_be_made(w)]
        
            