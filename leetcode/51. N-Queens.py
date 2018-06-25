"""https://leetcode.com/problems/n-queens/description/"""


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.rets = []
        qs = list(range(n))
        ts = []
        self.dp(qs, ts)
        retss = []
        for i, ret in enumerate(self.rets):
            retss.append([])
            for pos in ret:
                retss[i].append('.'*pos + 'Q' + '.' * (n-1 - pos))

        return retss

    def dp(self, qs, ts, depth=0):
        for q in qs:
            if q not in ts:
                for i in range(depth):
                    if ts[i] - q == depth - i or ts[i] - q == i-depth:
                        break
                else:
                    ts.append(q)
                    if len(ts) == self.n:
                        self.rets.append(ts.copy())
                    self.dp(qs, ts, depth+1)
                    del ts[-1]


if __name__ == '__main__':
    sl = Solution()
    ret = sl.solveNQueens(4)
    print(ret)
