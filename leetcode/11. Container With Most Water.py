"""https://leetcode.com/problems/container-with-most-water/descrip

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        i, j = 0, len(height) - 1

        while i < j:
            # 面积=最低高度*长度
            maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
            # 去掉高度相对低的
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

        return maxarea
