class Solution:
    def singleNonDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] == nums[mid-1]:
                if not mid % 2:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                if mid % 2:
                     right = mid - 1
                else:
                    left = mid
        return nums[left]

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2 | 1
            if nums[mid] == nums[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]


if __name__ == '__main__':
    sl = Solution()
    ret = sl.singleNonDuplicate([0,1,1,2,2,5,5])
    print(ret)