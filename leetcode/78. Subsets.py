"""Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

"""


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        return self.subsets(nums[:-1]) + [i+[nums[-1]] for i in self.subsets(nums[:-1])]  # 顺序排好的
        # return self.subsets(nums[1:]) + [i+[nums[0]] for i in self.subsets(nums[1:])]  # 顺序乱的


if __name__ == '__main__':
    sl = Solution()
    ret = sl.subsets([1, 2, 3])
    print(ret)
