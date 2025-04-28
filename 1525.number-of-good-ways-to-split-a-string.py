# You are given a string s.

# A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

# Return the number of good splits you can make in s.

 

# Example 1:

# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

class Solution:
    def numSplits(self, s: str) -> int:
        c = 0 
        l = s[:1]
        r = s[1:]
        ls = set(l)
        lc = len(ls)
        rs = set(r)
        rc = len(rs)
        dl = {}
        for j in l:
            dl[j] = dl.get(j,0) + 1
        dr = {}
        for j in r:
            dr[j] = dr.get(j,0) + 1
        i=1
        while i < len(s):
            if lc ==  rc:
                c += 1
            new_elem = s[i]
            if new_elem in ls:
                dl[new_elem] = dl.get(new_elem) + 1
            else:
                dl[new_elem] = dl.get(new_elem,0) + 1
                ls.add(new_elem)
                lc += 1
            
            dr[new_elem] = dr.get(new_elem) - 1

            if dr[new_elem] == 0:
                rs.remove(new_elem)
                rc -= 1
            i += 1

        return c
