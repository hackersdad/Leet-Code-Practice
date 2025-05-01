# Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        import copy
        def check_substring(parent,child):
            i = 0
            c = len(child)
            p = len(parent)
            while i <= p - c:
                if parent[i] == child[0]:
                    if parent[i:i+c] == child:
                        return True 
                i += 1
            return False
        
        seen = set()
        for i in range(len(words)):
            for j in words:
                if words[i] != j and len(j) < len(words[i]):
                    if check_substring(words[i],j) and j not in seen:
                        seen.add(j)
        return list(seen)


        
        