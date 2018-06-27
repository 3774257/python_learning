"""https://leetcode.com/problems/regular-expression-matching/description/

"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def dp(i, j):
            if i == ls and j == lp:
                return True
            if j+1 < lp and p[j+1] == '*':
                for k in range(i, ls + 1):
                    if p[j] == '.' or i >= ls or p[j] == s[i]:
                        if dp(k, j+2):
                            return True
                    else:
                        break
            if i >= ls or j >= lp:
                return False
            if s[i] == p[j] or p[j] == '.':
                return dp(i+1, j+1)
            return False

        i = j = 0
        ls = len(s)
        lp = len(p)
        return dp(i, j)


if __name__ == '__main__':
    s = "mississippi"
    p = "mis*is*p*."
    sl = Solution()
    ret = sl.isMatch(s, p)
    print(ret)
