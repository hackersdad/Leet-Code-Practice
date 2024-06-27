"""
Q => Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
    
        words.sort(key=lambda x : len(x))
        res = []
        for i in range(len(words[0])):
            if words[0][i] not in res :
                maintained_count = words[0].count(words[0][i])
                for j in range(1,len(words)):
                    if words[0][i] in words[j]:
                        maintained_count = min([words[j].count(words[0][i]), maintained_count])  
                    else:
                        maintained_count = 0
                        break

                l = [words[0][i]] * maintained_count   
                print(res)
                res.extend(l)  
        return res  