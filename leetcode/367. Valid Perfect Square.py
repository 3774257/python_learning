"""https://leetcode.com/problems/valid-perfect-square/description/"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        left = 0
        right = num
        while left <= right:
            mid = (left + right)//2
            midd = mid*mid
            if midd == num:
                return True
            elif midd > num:
                right = mid-1
            else:
                left = mid+1
        return False
