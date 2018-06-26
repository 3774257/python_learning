"""https://leetcode.com/problems/maximum-subarray/description/

"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsub = nums[0]
        cursum = 0
        for num in nums:
            cursum += num
            if cursum > maxsub:
                maxsub = cursum
            if cursum <= 0:
                cursum = 0
        return maxsub


if __name__ == '__main__':
    sl = Solution()
    inputs = [-2,1,-3,4,-1,2,1,-5,4]
    print(sl.maxSubArray(inputs))
