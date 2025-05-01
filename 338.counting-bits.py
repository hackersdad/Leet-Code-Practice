# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

class Solution:
    def countBits(self, n: int) -> List[int]:

        def binary_addition(a: str, b: str) -> str:
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            ans = ""
            c = 0
            while i >= 0 or j >= 0 or carry:
                sum = carry

                if i >= 0:
                    sum += int(a[i])
                    i -= 1
                if j >= 0:
                    sum += int(b[j])
                    j -= 1
                t = str(sum % 2)
                if t == '1':
                    c += 1
                ans = t + ans  
                carry = sum // 2 

            return [c,ans]
        ans = [0]
        b = "0"
        for i in range(n):
            t = binary_addition(b,"1")
            b = t[1]
            ans.append(t[0])

        return ans


        