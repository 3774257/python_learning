class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        count = collections.Counter(nums)
        mv = 0
        for n, v in count.items():
            if n+1 in count:
                s = v + count[n+1]
                if mv < s:
                    mv = s
        return mv


if __name__ == '__main__':
    sl = Solution()
    ret = sl.findLHS([1,3,2,2,5,2,3,7])
    print(ret)