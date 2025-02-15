# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

 

# Example 1:


# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indices_length = len(indices)
        temp = [''] * indices_length
        for i in range(indices_length):
            temp[indices[i]] = s[i] 
        return ''.join(temp)