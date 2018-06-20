"""https://leetcode.com/problems/valid-tic-tac-toe-state/description/"""


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """

        bb = ''.join(board)
        x = bb.count('X')
        o = bb.count('O')
        bb = list(bb)
        ss = [['X', 'X', 'X'], ['O', 'O', 'O']]
        spaces = [' ', ' ', ' ']
        if not (x == o or x == o+1):
            return False
        if o < 3:
            return True
        cnts = 0
        for i in range(3):
            if bb[3*i:3*i+3] in ss:  # ---
                if not ((bb[3*i] == 'X' and x == o+1) or(bb[3*i] == 'O' and x == o)):
                    return False
                cnts += 1
                bb[3*i:3*i+3] = spaces
            if bb[i:9:3] in ss:  # |
                if not ((bb[i] == 'X' and x == o+1) or (bb[i] == 'O' and x == o)):
                    return False
                cnts += 1
                bb[i:9:3] = spaces
        if bb[0:9:4] in ss:  # \
            if not ((bb[0] == 'X' and x == o+1) or(bb[0] == 'O' and x == o)):
                return False
            cnts += 1
            bb[0:9:4] = spaces
        if bb[2:7:2] in ss:  # /
            if not ((bb[2] == 'X' and x == o+1) or(bb[2] == 'O' and x == o)):
                return False
            cnts += 1
        return True if cnts <= 1 else False


if __name__ == '__main__':
    sl = Solution()
    ll = ["XOX", "OOX", "XO "]
    print(sl.validTicTacToe(ll))
