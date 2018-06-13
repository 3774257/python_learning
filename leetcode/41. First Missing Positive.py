"""https://leetcode.com/problems/first-missing-positive/description/
Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and uses constant extra space.


"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i, c in enumerate(nums):
            if c < 0 or c >= n:
                nums[i] = 0
        for c in nums:
            nums[c % n] += n
        for i, c in enumerate(nums):
            if c//n == 0:
                return i
        return n


sl = Solution()
print(sl.firstMissingPositive([1,2,0]))