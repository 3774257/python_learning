"""https://leetcode.com/problems/spiral-matrix-ii/description/
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        import math
        rets = []
        for i in range(n):
            rets.append([0] * n)
        loops = math.ceil(n/2)
        nums = iter(range(1, n*n+1))
        for i in range(loops):
            for j in range(i, n-i):
                rets[i][j] = next(nums)
            for j in range(i+1, n-i):
                rets[j][n-1-i] = next(nums)
            for j in range(n-i-2,i-1,-1):
                rets[n-1-i][j] = next(nums)
            for j in range(n-i-2, i, -1):
                rets[j][i] = next(nums)
        return rets


if __name__ == '__main__':
    sl = Solution()
    ret = sl.generateMatrix(3)
    print(ret)
