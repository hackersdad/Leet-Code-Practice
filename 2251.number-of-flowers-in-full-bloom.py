# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

 

# Example 1:


# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        # d = {}
        # for f in flowers:
        #     start = f[0]
        #     end = f[1]
        #     for j in range(start,end+1):
        #         d[j] = d.get(j,0) + 1

        # ans = []
        # for p in people:
        #     if p in d:
        #         t = d[p]
        #     else:
        #         t = 0
        #     ans.append(t)
        # return ans
        #  Above implementatioin is not memory efficient in large cases

        # ans = [0] * len(people)

        # for i in flowers:
        #     for p in range(len(people)):
        #         t = ans[p]
        #         if people[p] >= i[0] and people[p] <= i[1]:
        #             t += 1
        #             ans[p] = t
        # return ans

        # this above implementation is not time efficient

        start = []
        end = []
        for i in flowers:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        
        def b_search(item,arr,flag=0):
            l = 0
            h = len(arr) - 1
            a = -1
            while l <= h:
                m = (l+h)//2
                if flag == 0:
                    if arr[m] <= item:
                        l = m + 1
                        a = m
                    else:
                        h = m - 1
                else:
                    if arr[m] < item:
                        l = m + 1
                        a = m
                    else:
                        h = m - 1
            return 0 if a == -1 else a + 1
        ans = []
        for p in people:
            # flowers start <= p time
            s =  b_search(p,start)
            # flowers end < p time
            e =  b_search(p,end,1)
            ans.append(s-e)
        
        return ans








        