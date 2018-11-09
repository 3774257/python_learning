class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = range(1, n+1)
        flag = 1
        while len(n) > 1:
            #print(n)
            if flag:
                n = n[1::2]
            else:
                start = len(n) % 2
                n = n[start::2]
            flag ^= True
        return n[0]











if __name__ == '__main__':
    sl = Solution()
    for nn in range(99, 100):
        print(nn, sl.lastRemaining(nn))
