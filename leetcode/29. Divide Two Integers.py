"""https://leetcode.com/problems/divide-two-integers/description/
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 231 − 1
    when the division result overflows.
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if dividend < 0:
            flag = -flag
            dividend = -dividend
        if divisor < 0:
            flag = -flag
            divisor = -divisor

        if divisor == 1:
            rets = dividend if flag == 1 else -dividend
            return max(min(2147483647, rets), -2147483648)

        rets = 0
        tmpdiv = divisor
        while dividend >= tmpdiv + tmpdiv:
            tmpdiv <<= 1

        while tmpdiv >= divisor:
            while dividend < tmpdiv and tmpdiv > divisor:
                rets <<= 1
                tmpdiv >>= 1
            t = 1 if dividend >= tmpdiv else 0
            if t:
                dividend -= tmpdiv
            rets += rets + t
            tmpdiv >>= 1

        return rets if flag == 1 else -rets


sl = Solution()
print(sl.divide(300000002, -3))
