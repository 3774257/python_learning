class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        from collections import Counter
        c_board = Counter([c for row in board for c in row])
        c_word = Counter(word)
        for c in c_word:
            if c not in c_board or c_board[c] < c_word[c]:
                return False

        m = len(board)
        n = len(board[0])
        lw = len(word)
        if not n or not word:
            return False

        # def dfs(i, j, k):
        #     if k == lw:
        #         return True
        #     if j < n-1 and board[i][j+1] == word[k]:  # right
        #         board[i][j+1] = k
        #         ret = dfs(i, j+1, k+1)
        #         if ret:
        #             return ret
        #         board[i][j+1] = word[k]
        #     elif i < m-1 and board[i+1][j] == word[k]:  # down
        #         board[i+1][j] = k
        #         ret = dfs(i+1, j, k+1)
        #         if ret:
        #             return ret
        #         board[i+1][j] = word[k]
        #     elif j > 0 and board[i][j-1] == word[k]:  # left
        #         board[i][j-1] = k
        #         ret = dfs(i, j-1, k+1)
        #         if ret:
        #             return ret
        #         board[i][j-1] = word[k]
        #     elif i > 0 and board[i-1][j] == word[k]:  # up
        #         board[i-1][j] = k
        #         ret = dfs(i-1, j, k+1)
        #         if ret:
        #             return ret
        #         board[i-1][j] = word[k]
        #     return False
        #
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] != word[0]:
        #             continue
        #         board[i][j] = 0
        #         ret = dfs(i, j, 1)
        #         if ret:
        #             return ret
        #         board[i][j] = word[0]
        #
        # return False
        def dfs(i, j, k):
            if k == lw:
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[k]:
                return False
            board[i][j] = ' '
            ret = dfs(i, j+1, k+1) or dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
            if ret:
                return True
            board[i][j] = word[k]
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    sl = Solution()
    board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = 'ABCCED'
    rets = sl.exist(board, word)
    print(rets)
