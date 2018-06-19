"""
https://leetcode.com/problems/trapping-rain-water/description/
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        left = 0
        right = len(height) - 1
        waters = 0

        j = right - 1

        while left < right:
            if height[left] <= height[right]:
                i = left + 1
                while height[left] > height[i]:
                    waters += height[left] - height[i]
                    i += 1
                left = i
            else:
                i = right - 1
                while height[right] > height[i]:
                    waters += height[right] - height[i]
                    i -= 1
                right = i
        return waters


