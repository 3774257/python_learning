"""https://leetcode.com/problems/reverse-integer/description/
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            x = -x
            flag = True
        else:
            flag = False

        r = int(str(x)[::-1])
        if flag:
            r *= -1
        if r < -2147483648 or r > 2147483647:
            return 0
        else:
            return r
        # 第二种方法计算
        r = 0
        while x > 0:
            x, d = divmod(x, 10)
            r = r * 10 + d
        if flag:
            r = -r
        if r < -2147483648 or r > 2147483647:
            return 0
        else:
            return r

