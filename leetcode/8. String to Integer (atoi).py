class Solution:
    def myAtoi(self, strs):
        """
        :type str: str
        :rtype: int
        """
        # n = len(strs)
        # if not n:
        #    return 0

        i = 0
        #flag = 0
        while strs[i:] and strs[i] in ' ':
            i += 1
        if strs[i:] and strs[i] in '+-':
            j = i+1
        else:
            j = i
        while strs[j:] and strs[j] in '0123456789':
            j += 1

        strs = strs[i:j]
        if strs[0:1] == '-':
            flag = -1
            strs = strs[1:]
        elif strs[0:1] == '+':
            flag = 1
            strs = strs[1:]
        else:
            flag = 1

        if not strs.isdigit():
            return 0
        ret = flag * int(strs)
        if ret > 2147483647:
            return 2147483647
        if ret < -2147483648:
            return -2147483648
        return ret


if __name__ == '__main__':
    s = Solution()
    l = '+10a s'
    print(s.myAtoi(l))
