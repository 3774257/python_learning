"""https://leetcode.com/problems/zigzag-conversion/description/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
And then read line by line: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

"""
import sys

class Solution:
    # 结果放str中，效率竟然比list高
    def convert2(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        n = len(s)
        step = 2*numRows-2
        rets = s[::step]
        mid = []
        for i in range(1, numRows-1):
            j = i
            while j < n:
                rets += s[j:j+step-i*2+1:step-i*2]
                j += step
        rets += s[numRows-1::step]
        return rets

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

    def convert3(self,s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        step = 2 * numRows - 2
        rets = s[::step]
        tailn = n // (numRows * 2 - 2) * (numRows * 2 - 2)
        for i in range(1, numRows - 1):
            t1 = s[i:tailn:step]
            t2 = s[step - i:tailn:step]
            for t in zip(t1, t2):
                rets += t[0] + t[1]
            rets += s[tailn + i::step]
            rets += s[tailn + step - i::step]

        rets += s[numRows - 1::step]
        return rets


sl = Solution()
s = "PAYPALISHIRINGJDLSFJFJ39FJSJFSJDFLASDFJ0AFJ0SAFJ0ADJFASDFJ0ASDJF0AJFE94JR3PRJDFJ0SDJFSFSF"
numRows = 4
print(sl.convert(s, numRows))
print(sl.convert2(s, numRows))
print(sl.convert3(s, numRows))
