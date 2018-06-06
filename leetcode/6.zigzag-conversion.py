"""https://leetcode.com/problems/zigzag-conversion/description/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
And then read line by line: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        step = 2 * numRows - 2
        rets = ''
        head = s[::step]
        mid = []
        for i in range(1, numRows - 1):
            j = i
            while j < n:
                mid += s[j:j + step - i * 2 + 1:step - i * 2]
                j += step
        tail = s[numRows - 1::step]
        rets = head + ''.join(mid) + tail
        return rets

