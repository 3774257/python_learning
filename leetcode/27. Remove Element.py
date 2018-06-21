"""https://leetcode.com/problems/remove-element/description/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        if j < 0:
            return 0
        if j == 0:
            if nums[0] == val:
                return 0
            else:
                return 1
        while i < j:
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i

    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for c in nums:
            if c != val:
                nums[i] = c
                i += 1
        return i


if __name__ == '__main__':
    sl = Solution()
    ss = [3, 3, 2]
    ret = sl.removeElement(ss, 2)
    print(ss[:ret])
