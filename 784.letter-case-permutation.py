# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(index,cr):
            
            if index == len(s):
                res.append(cr[:])
                return

            while index < len(s) and s[index] in ['1','2','3','4','5','6','7','8','9','0']:
                cr += s[index]
                index += 1
            
            if index == len(s):
                res.append(cr[:])
                return

            old = s[index]
            if ord(s[index]) < 97:
                new = chr(ord(s[index]) + 32)
            else:
                new = chr(ord(s[index]) - 32)
            cr += new
            backtrack(index + 1, cr)
            t = cr[:-1]
            t += old
            cr = t
            backtrack(index + 1, cr)
        
        backtrack(0,"")

        return res








        