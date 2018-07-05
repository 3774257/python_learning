"""https://leetcode.com/problems/unique-paths-ii/description/
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        walks = [[0 for _ in range(n)] for _ in range(m)]
        walks[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for j in range(1, n):
            walks[0][j] = walks[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, m):
            walks[i][0] = 0 if obstacleGrid[i][0] else walks[i - 1][0]
            for j in range(1, n):
                walks[i][j] = 0 if obstacleGrid[i][j] else walks[i - 1][j] + walks[i][j - 1]

        return walks[-1][-1]
        '''
        from functools import lru_cache
        m = len(obstacleGrid)-1
        n = len(obstacleGrid[0])-1

        @lru_cache(maxsize=128000)
        def walks(i, j):
            if obstacleGrid[i][j]:
                return 0
            if i == m and j == n:
                return 1
            return (walks(i+1, j) if i<m else 0) +(walks(i, j+1) if j<n else 0)

        return walks(0, 0)'''


if __name__ == '__main__':
    sl = Solution()
    maps = [[0,0,0],[0,1,0],[0,0,0]]

    ret = sl.uniquePathsWithObstacles(maps)
    print(ret)