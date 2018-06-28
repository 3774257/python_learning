"""https://leetcode.com/problems/sum-of-square-numbers/description/
"""
# Given a non-negative integer c, your task is to decide whether therere two integers a and b such that a2 + b2 = c.


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        for i in range(int(sqrt(c//2)),int(sqrt(c))+1):
            j = sqrt(c - i*i)
            if j == int(j):
                return True
        return False
