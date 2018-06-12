"""https://leetcode.com/problems/4sum/description/
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        r = []
        nums.sort()
        for i in range(n - 3):
            if nums[i] * 4 > target:
                break
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                if target < nums[i] + nums[j] * 3:
                    break
                while k < l:
                    left = target - nums[i] - nums[j] - nums[k]
                    while k < l and left < nums[l]:
                        l -= 1
                    if left == nums[l] and k < l:
                        if [nums[i], nums[j], nums[k], nums[l]] not in r:
                            r.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1

        return r


    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.n = len(nums)
        r = []
        nums.sort()
        for i in range(self.n - 3):
            if nums[i] * 4 > target:
                break
            for j in range(i + 1, self.n - 2):
                if target < nums[i] + nums[j] * 3:
                    break
                k = j + 1
                l = self.bin_search(nums, target - nums[i] - nums[j] - nums[k], k + 1, self.n - 1)
                while k < l:
                    left = target - nums[i] - nums[j] - nums[k]
                    while k < l and left < nums[l]:
                        l -= 1
                    if left == nums[l] and k < l:
                        if [nums[i], nums[j], nums[k], nums[l]] not in r:
                            r.append([nums[i], nums[j], nums[k], nums[l]])
                        l -= 1
                    k += 1

        return r

    def bin_search(self, nums, target, left, right):
        if target <= nums[left]:
            return left
        elif target >= nums[right]:
            return right
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.bin_search(nums, target, left, mid - 1)
        else:
            return self.bin_search(nums, target, mid + 1, right)