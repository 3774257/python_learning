"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        pos = 0
        c = None
        for n in nums:
            if n != c:
                nums[pos] = n
                c = n
                pos += 1

        return pos
