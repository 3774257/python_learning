class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        nums2 = []
        for num in nums:
            if not nums2 or num != nums2[-1]:
                nums2.append(num)
        if len(nums2) >=2 and nums[0] == nums[-1]:
            del nums2[-1]
        nums = nums2
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            elif nums[left]<=nums[mid]<target or target<nums[left]<=nums[mid] or nums[mid]<target<=nums[right]:
                    left = mid+1
            else:
                right = mid-1
        return False
