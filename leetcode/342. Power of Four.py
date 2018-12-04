class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and ((num & (num - 1)) == 0) and ((num & 0x55555555) == num)

    def isPowerOfFour2(self, num):
        if num <= 0:
            return False
        while num > 1:
            if num & 0x03:
                return False
            num >>= 2
        return True
