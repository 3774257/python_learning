class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
        maxlen = 1
        t = 0
        dd = {}
        for i, c in enumerate(s):
            if c in dd:
                tlen = i - t
                if t <= dd[c]:
                    t = dd[c]+1
                if maxlen < tlen:
                    maxlen = tlen
            dd[c] = i
        if n - t > maxlen:
            maxlen = n - t
        return maxlen


ss = Solution()
print(ss.lengthOfLongestSubstring("abcabcbb"))
