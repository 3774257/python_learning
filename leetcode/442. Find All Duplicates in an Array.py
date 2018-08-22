"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
"""


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rets = []
        n = len(nums)
        for num in nums:
            i = (num-1)%n
            if nums[i] > n:
                rets.append(i+1)
            else:
                nums[i] += n
        return rets


if __name__ == '__main__':
    sl = Solution()
    l = [4,3,2,7,8,2,3,1]
    print(sl.findDuplicates(l))
