class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[left]<=nums[mid]<target or target<nums[left]<=nums[mid] or nums[mid]<target<=nums[right]:
                    left = mid+1
            else:
                right = mid-1
        return -1


if __name__ == '__main__':
    sl = Solution()
    ret = sl.search([5,1,3],3)
    print(ret)
