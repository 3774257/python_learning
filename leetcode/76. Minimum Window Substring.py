"""https://leetcode.com/problems/minimum-window-substring/description/
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dt = {}
        mw, rets = 999999, ""
        for c in t:
            if c not in dt:
                dt[c] = [-1, -1, []]
            else:
                dt[c][0] -= 1
        for i, c in enumerate(s):
            if c in dt:
                dt[c][0] += 1
                dt[c][2].append(i)
                if dt[c][0] >= 0:
                    dt[c][1] = dt[c][2][dt[c][0]]
                if min(dt.values(), key=lambda x:x[0])[0] >= 0:
                    mi = min(dt.values(), key=lambda x:x[1])[1]

                    if i - mi + 1 < mw:
                        mw = i - mi + 1
                        rets = s[mi:i+1]
        return rets


if __name__ == '__main__':
    sl = Solution()
    ret = sl.minWindow("ADOBECODEBANC","ABC")
    print(ret)
