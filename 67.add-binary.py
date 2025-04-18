# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        ap = len(a) -1
        bp = len(b) -1
        ans = ""
        carry  = 0
        while ap >= 0 or bp >= 0:

            if ap >= 0:
                ta = a[ap]
            else:
                ta = 0
            if bp >= 0:
                tb = b[bp]
            else:
                tb = 0
            temp = int(ta) + int(tb) + carry
            if temp > 1:
                if temp == 2 : 
                    carry = 1
                    res = 0
                else:
                    carry  = 1
                    res = 1
            else:
                carry = 0
                res = temp
            ans += str(res)
            
            ap -= 1
            bp -= 1
        if carry > 0:
            ans += str(carry)
        
        return ans[::-1]
           


        