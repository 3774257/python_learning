"""https://leetcode.com/problems/length-of-last-word/description/
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = 'abcdefghijklmnopqrstuvwxyz'
        schars = set(chars + chars.upper())
        isword = False
        rets = 0
        for c in s[::-1]:
            if isword == False and c in schars:
                isword = True
                rets += 1
            elif isword == True and c in schars:
                rets += 1
            elif isword == True and c not in schars:
                return rets
        return rets
