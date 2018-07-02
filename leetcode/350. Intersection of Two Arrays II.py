"""https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        d = defaultdict(int)
        rets = []
        for n in nums1:
            d[n] += 1
        for n in nums2:
            if d[n]:
                rets.append(n)
                d[n] -= 1
        return rets
