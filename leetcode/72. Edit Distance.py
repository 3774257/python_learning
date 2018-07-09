"""https://leetcode.com/problems/edit-distance/description/
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        from functools import lru_cache
        m, n = len(word1), len(word2)

        @lru_cache(maxsize=10000)
        def f(i=0, j=0):
            while i < m and j < n and word1[i] == word2[j]:
                i += 1
                j += 1
            if i == m or j == n:
                return m+n-i-j
            return 1 + min(f(i+1, j), f(i+1, j+1), f(i, j+1))

        return f(0, 0)


if __name__ == '__main__':
    sl = Solution()
    ret = sl.minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine")
    print(ret)
