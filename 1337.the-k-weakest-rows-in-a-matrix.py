# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

# Example 1:

# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        # d = {}
        # for i in range(len(mat)):
        #     temp = sum(mat[i])
        #     d[i] = temp
        # v = list(d.values())
        # v.sort()
        # ans = []
        # for n in range(k):
        #     for j in d:
        #         if d[j] == v[n]:
        #             ans.append(j)
        #             del d[j]
        #             break
        # return ans

        tl = []
        for i in range(len(mat)):
            tl.append((sum(mat[i]),i))   # used tuple to keep track of the sum as well as id, when sorting it compares first lemnt if same tehn compares second, which fits in our case
        tl.sort()
        ans = []
        for j in range(k):
            ans.append(tl[j][1])
        return ans


        