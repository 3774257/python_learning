"""https://leetcode.com/problems/n-queens-ii/description/"""


class Solution:

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self.rets = 0
        qs = list(range(n))
        ts = []
        self.dp(qs, ts)
        return self.rets

    def dp(self, qs, ts, depth=0):
        for q in qs:
            if q not in ts:
                for i in range(depth):
                    if ts[i] - q == depth - i or ts[i] - q == i-depth:
                        break
                else:
                    ts.append(q)
                    if len(ts) == self.n:
                        self.rets += 1
                    self.dp(qs, ts, depth+1)
                    del ts[-1]
