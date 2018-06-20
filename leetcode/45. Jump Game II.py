"""https://leetcode.com/problems/jump-game-ii/description/
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums)-1
        steps = 0   # 步数
        farest = 0  # 前一步的最远距离
        curstepcur = 0  # 最远距离
        for i, step in enumerate(nums):
            farest = max(i + step, farest)
            if farest >= end:
                return steps+1
            if curstepcur == i:
                steps += 1
                curstepcur = farest
        return steps


if __name__ == '__main__':
    sl = Solution()
    nums = [2,3,1,1,4]
    print(sl.jump(nums))

