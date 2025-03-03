# You are given an integer array deck where deck[i] represents the number written on the ith card.

# Partition the cards into one or more groups such that:

# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

 

# Example 1:

# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:

# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        def hcf(arr):
            min_val = min(arr)
            for mv in range(min_val,1,-1):
                flag = False
                for v in arr:
                    if v%mv == 0:
                        flag = True
                    else:
                        flag = False
                        break
                if flag == True:
                    return mv
            return -1

        d = {}
        for i in deck:
            if i in d:
                temp = d[i]
                d[i] = temp + 1
            else:
                d[i] = 1
        l = []
        for j in d:
            l.append(d[j])

        if hcf(l) > 1:
            return True
        else:
            return False
        