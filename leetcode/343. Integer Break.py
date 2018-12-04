class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        threes = (n - 2) // 3
        left = n - threes * 3
        return 3 ** threes * left
