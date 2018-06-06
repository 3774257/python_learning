"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


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
