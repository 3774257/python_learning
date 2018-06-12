"""https://leetcode.com/problems/3sum/description/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        n = len(nums)
        if n < 3:
            return results
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                cha = -nums[i] - nums[j]
                if cha < 0:
                    break
                while cha < nums[k]:
                    k -= 1
                    if j >= k:
                        break
                else:
                    if cha == nums[k]:
                        results.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                    j += 1

        return results


