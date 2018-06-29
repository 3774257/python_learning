"""https://leetcode.com/problems/length-of-last-word/description/
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        space = ' '
        isword = False
        rets = 0
        for c in s[::-1]:
            if isword == False and c != space:
                isword = True
                rets += 1
            elif isword == True and c != space:
                rets += 1
            elif isword == True and c == space:
                return rets
        return rets
