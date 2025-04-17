# You are given a string s. Reorder the string using the following algorithm:

# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

# Return the resulting string after reordering s using this algorithm.

 

# Example 1:

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
# Example 2:

# Input: s = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

class Solution:
    def sortString(self, s: str) -> str:
        

        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        unique = list(d.keys())
        unique.sort()
        res = ""
        tracker = 0
        while len(d) > 0:
            if tracker % 2 == 0:
                for i in range(0,len(unique)):
                    if unique[i] in d:
                        res += unique[i]
                        d[unique[i]] = d.get(unique[i]) - 1
                        if d[unique[i]] == 0:
                            del d[unique[i]]
                tracker += 1
            else:
                for i in range(len(unique)-1,-1,-1):
                    if unique[i] in d:
                        res += unique[i]
                        d[unique[i]] = d.get(unique[i]) - 1
                        if d[unique[i]] == 0:
                            del d[unique[i]]
                tracker += 1
        return res

