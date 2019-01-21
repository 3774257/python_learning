import numpy as np
# from collections import Counter
# sudoku = [[0,0,7,0,6,0,5,0,0],[0, 0, 0, 3, 0, 0, 0, 2, 6], [0, 0, 9, 0, 0, 7, 0, 0, 3], [5, 4, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 6, 0, 0, 0, 8, 0], [2, 7, 0, 1, 0, 8, 4, 0, 0], [0, 0, 0, 0, 0, 0, 1, 5, 0], [6, 0, 0, 9, 0, 0, 0, 0, 0], [0, 1, 0, 7, 0, 0, 0, 0, 0]]
# sudoku = [[0,0,0,1,0,0,0,0,0],[0,8,2,7,0,0,0,0,0],[1,0,0,0,0,0,9,0,0],[9,0,0,2,0,0,0,0,5],[0,7,0,0,0,0,0,0,9],[0,6,1,8,3,0,0,7,0],[0,0,0,0,0,1,0,5,0],[0,0,0,0,2,4,0,9,6],[0,1,3,0,0,0,0,0,0]]
# sudoku = [[0,9,6,7,5,0,0,8,0],[8,0,0,0,6,0,0,0,2],[0,3,0,8,0,0,0,0,5],[5,0,0,2,0,8,0,0,0],[0,0,0,1,0,9,0,0,0],[0,7,4,0,0,0,0,0,0],[0,0,0,0,0,4,0,0,0],[0,0,0,0,0,0,9,0,4],[0,0,7,0,0,0,6,0,3]]
# sudoku = [[1,0,0,0,0,2,0,0,0],[0,7,4,0,0,0,0,9,0],[0,0,9,0,0,0,7,1,2],[5,0,0,0,6,0,0,8,0],[0,8,0,5,0,0,0,0,3],[0,2,3,9,0,0,6,0,0],[0,3,5,0,0,0,0,0,0],[7,0,0,8,0,0,0,0,0],[0,0,0,4,3,0,0,0,5]]
# sudoku = [[7,0,0,0,3,0,1,0,9],[0,1,9,0,0,4,0,0,0],[0,0,0,0,7,0,0,0,0],[0,4,0,0,0,3,5,0,0],[2,0,7,0,4,8,6,0,0],[0,0,1,0,0,5,0,0,0],[6,7,0,0,0,0,0,0,3],[0,0,2,0,0,0,0,0,6],[5,0,0,0,0,0,0,2,0]]
sudoku = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku = np.array(sudoku)


def dfs(m=0, n=0):
    for i in range(m, 9):
        for j in range(n if i == m else 0, 9):
            if sudoku[i, j] != 0:
                continue
            for value in nums:
                if value in sudoku[i, :] or value in sudoku[:, j] or value in sudoku[i-i%3:i-i%3+3, j-j%3:j-j%3+3]:
                    continue
                sudoku[i, j] = value
                if i == 8 and j == 8:
                    print("DFS Find:\n", sudoku)
                    exit()
                else:
                    dfs(i, j)
            sudoku[i, j] = 0
            return

dfs(0, 0)