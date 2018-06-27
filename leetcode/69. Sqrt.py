class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left = 0
        right = x
        while left < right:
            mid = (left + right) // 2
            cha = mid * mid - x
            if cha > 0:
                right = mid
            elif cha == 0:
                return mid
            elif (mid + 1) * (mid + 1) > x:
                return mid
            else:
                left = mid


if __name__ == '__main__':
    sl = Solution()
    ret = sl.mySqrt(8)
    print(ret)