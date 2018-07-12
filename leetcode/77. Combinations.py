class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return list(combinations(range(1, n+1), k))

"""
        rets = []
        nums = []

        def f(next, k):
            for i in range(next, n + 1):
                nums.append(i)
                if k == 1:
                    rets.append(nums[:])
                else:
                    f(i + 1, k - 1)
                nums.pop()

        f(1, k)
        return rets
"""

if __name__ == '__main__':
    sl = Solution()
    ret = sl.combine(4, 2)
    print(ret)
