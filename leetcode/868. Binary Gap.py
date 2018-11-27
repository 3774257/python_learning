class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)
        prei = None
        maxlen = 0
        i, n = 2, len(s)
        while i < n:
            if s[i] != '1':
                i += 1
                continue
            j = i+1
            while j < n:
                if s[j] != '1':
                    j += 1
                    continue
                maxlen = max(maxlen, j-i)
                i = j
                break
            else:
                return maxlen
        return maxlen


if __name__ == '__main__':
    sl = Solution()
    ret = sl.binaryGap(22)
    print(ret)