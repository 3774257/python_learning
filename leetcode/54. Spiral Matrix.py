"""https://leetcode.com/problems/spiral-matrix/description/
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        lops = min(m // 2, n // 2)
        rets = []

        for i in range(lops):
            rets.extend(matrix[i][i:n - i])
            for j in range(i + 1, m - 1 - i):
                rets.append(matrix[j][n - i - 1])
            rets.extend(matrix[m - i - 1][n - i - 1:i:-1])
            for j in range(m - 1 - i, i, -1):
                rets.append(matrix[j][i])
        if lops*2 < m <= n:
            rets.extend(matrix[lops][lops:n-lops])
        elif lops*2 < n < m:
            for j in range(lops, m - lops):
                rets.append(matrix[j][lops])
        return rets


if __name__ == '__main__':
    sl = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ret = sl.spiralOrder(m)
    print(ret)
