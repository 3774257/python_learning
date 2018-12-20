import numpy as np
from collections import Counter
# sudoku = [[0,0,7,0,6,0,5,0,0],[0, 0, 0, 3, 0, 0, 0, 2, 6], [0, 0, 9, 0, 0, 7, 0, 0, 3], [5, 4, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 6, 0, 0, 0, 8, 0], [2, 7, 0, 1, 0, 8, 4, 0, 0], [0, 0, 0, 0, 0, 0, 1, 5, 0], [6, 0, 0, 9, 0, 0, 0, 0, 0], [0, 1, 0, 7, 0, 0, 0, 0, 0]]
# sudoku = [[0,0,0,1,0,0,0,0,0],[0,8,2,7,0,0,0,0,0],[1,0,0,0,0,0,9,0,0],[9,0,0,2,0,0,0,0,5],[0,7,0,0,0,0,0,0,9],[0,6,1,8,3,0,0,7,0],[0,0,0,0,0,1,0,5,0],[0,0,0,0,2,4,0,9,6],[0,1,3,0,0,0,0,0,0]]
# sudoku = [[0,9,6,7,5,0,0,8,0],[8,0,0,0,6,0,0,0,2],[0,3,0,8,0,0,0,0,5],[5,0,0,2,0,8,0,0,0],[0,0,0,1,0,9,0,0,0],[0,7,4,0,0,0,0,0,0],[0,0,0,0,0,4,0,0,0],[0,0,0,0,0,0,9,0,4],[0,0,7,0,0,0,6,0,3]]
# sudoku = [[1,0,0,0,0,2,0,0,0],[0,7,4,0,0,0,0,9,0],[0,0,9,0,0,0,7,1,2],[5,0,0,0,6,0,0,8,0],[0,8,0,5,0,0,0,0,3],[0,2,3,9,0,0,6,0,0],[0,3,5,0,0,0,0,0,0],[7,0,0,8,0,0,0,0,0],[0,0,0,4,3,0,0,0,5]]
sudoku = [
    [7,0,0,0,3,0,1,0,9],
    [0,1,9,0,0,4,0,0,0],
    [0,0,0,0,7,0,0,0,0],
    [0,4,0,0,0,3,5,0,0],
    [2,0,7,0,4,8,6,0,0],
    [0,0,1,0,0,5,0,0,0],
    [6,7,0,0,0,0,0,0,3],
    [0,0,2,0,0,0,0,0,6],
    [5,0,0,0,0,0,0,2,0]
]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = set(nums)

sudoku = np.array(sudoku)

possible_t = dict()


def delvfrommatrx(i, j, value):
    for m in range(9):
        if (i, m) in possible_t and value in possible_t[(i, m)]:
            possible_t[(i, m)].remove(value)
        if (m, j) in possible_t and value in possible_t[(m, j)]:
            possible_t[(m, j)].remove(value)
    for m in range(i - i % 3, i - i % 3 + 3):
        for n in range(j - j % 3, j - j % 3 + 3):
            if (m, n) in possible_t and value in possible_t[(m, n)]:
                possible_t[(m, n)].remove(value)


# init possible_table
for i in range(9):
    for j in range(9):
        if sudoku[i, j] != 0:
            continue
        t = set()
        for m in range(9):
            t.add(sudoku[i, m])
            t.add(sudoku[m, j])
        for m in range(i-i % 3, i-i % 3 + 3):
            for n in range(j - j % 3, j - j % 3 + 3):
                t.add(sudoku[m, n])
        possible_t[(i, j)] = nums - t
        print((i, j), sudoku[i, j], possible_t[(i, j)])

# for k, v in possible_t.items():
#     print(k, v)

change = True
while possible_t and change:
    change = False
    for k, v in possible_t.items():
        if len(v) != 1:
            continue
        change = True
        print("Find:", k, v)
        i, j = k
        value = v.pop()
        sudoku[i, j] = value
        delvfrommatrx(i, j, value)
        del possible_t[k]
        break
    # check line
    for i in range(9):
        t = []
        for j in range(9):
            if (i, j) in possible_t:
                t.extend(list(possible_t[i, j]))
        c = Counter(t)
        for value in c:
            if c[value] != 1:
                continue
            change = True
            # find i, j
            for j in range(9):
                if (i, j) in possible_t and value in possible_t[i, j]:
                    print("Find Line:", (i, j), value)
                    sudoku[i, j] = value
                    delvfrommatrx(i, j, value)
                    del possible_t[(i, j)]
    # check Column
    for j in range(9):
        t = []
        for i in range(9):
            if (i, j) in possible_t:
                t.extend(list(possible_t[i, j]))
        c = Counter(t)
        for value in c:
            if c[value] != 1:
                continue
            change = True
            # find i, j
            for i in range(9):
                if (i, j) in possible_t and value in possible_t[i, j]:
                    print("Find Col:", (i, j), value)
                    sudoku[i, j] = value
                    delvfrommatrx(i, j, value)
                    del possible_t[(i, j)]
    # check block:
    for m in range(3):
        for n in range(3):
            t = []
            for i in range(m*3, m*3+3):
                for j in range(n*3, n*3+3):
                    if (i, j) in possible_t:
                        t.extend(list(possible_t[i, j]))
            c = Counter(t)
            for value in c:
                if c[value] != 1:
                    continue
                change = True
                # find i, j
                for i in range(m * 3, m * 3 + 3):
                    for j in range(n * 3, n * 3 + 3):
                        if (i, j) in possible_t and value in possible_t[i, j]:
                            print("Find gong:", (i, j), value)
                            sudoku[i, j] = value
                            delvfrommatrx(i, j, value)
                            del possible_t[(i, j)]

print(len(possible_t), possible_t)
print(sudoku)

if not len(possible_t):
    exit()


def dfs(m=0, n=0):
    for i in range(m, 9):
        for j in range(n if i == m else 0, 9):
            if sudoku[i, j] == 0:
                for value in possible_t[(i, j)]:
                    if value in sudoku[i, :] or value in sudoku[:, j] or value in sudoku[i-i%3:i-i%3+3, j-j%3:j-j%3+3]:
                        continue
                    sudoku[i, j] = value
                    if i == 8 and j == 8:
                        print("DFS Find:\n", sudoku)
                    else:
                        dfs(i, j)
                sudoku[i, j] = 0
                return

dfs(0, 0)