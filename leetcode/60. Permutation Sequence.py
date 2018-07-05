"""https://leetcode.com/problems/permutation-sequence/description/
"""
import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        s = ""
        ls = list(range(1,n+1))
        facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        for i in range(n-1,-1,-1):
            fact = facts[i]
            s += str(ls.pop(k//fact))
            k = k % fact
        return s


if __name__ == '__main__':
    sl = Solution()
    rets = sl.getPermutation(4, 3)
    print(rets)
