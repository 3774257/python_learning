"""https://leetcode.com/problems/count-and-say/description/
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rets = '1'
        while n > 1:
            tmp = ''
            tn = 0
            for c in rets:
                if not tn:
                    tn = 1
                    tc = c
                elif c == tc:
                    tn += 1
                else:
                    tmp += str(tn) + tc
                    tn = 1
                    tc = c
            tmp += str(tn) + tc
            rets = tmp
            n -= 1
        return rets
