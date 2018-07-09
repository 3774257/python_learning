class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeropos = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeropos.add((i, -1))
                    zeropos.add((-1, j))
        for i, j in zeropos:
            if i == -1:
                for i in range(m):
                    matrix[i][j] = 0
            else:
                for j in range(n):
                    matrix[i][j] = 0
