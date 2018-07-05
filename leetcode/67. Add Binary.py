"""https://leetcode.com/problems/add-binary/description/
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return bin(eval('0b'+a)+eval('0b'+b))[2:]
        carry = 0
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        m = len(a)
        n = len(b)
        rets = ''
        i = 0
        j = min(m, n)
        for i in range(j):
            carry, c = divmod(int(a[i]) + int(b[i]) + carry, 2)
            rets = str(c) + rets
        for i in range(j, m):
            carry, c = divmod(int(a[i]) + carry, 2)
            rets = str(c) + rets
        for i in range(j, n):
            carry, c = divmod(int(b[i]) + carry, 2)
            rets = str(c) + rets
        if carry:
            rets = str(carry) + rets
        return rets
