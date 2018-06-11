"""https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

返回字符串数组中最长公共前缀字符串
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ''
        if len(strs) == 1:
            return strs[0]

        ret = ''
        # strs.sort(key=lambda x:len(x))
        for i in range(1, len(strs[0]) + 1):
            for k in range(1, len(strs)):
                if strs[0][:i] != strs[k][:i]:
                    return ret
            else:
                if len(ret) < i:
                    ret = strs[0][:i]
        return ret


if __name__ == '__main__':
    sl = Solution()
    strs = ["c", "c"]
    print(sl.longestCommonPrefix(strs))
