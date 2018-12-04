class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = list(s)
        left, right = 0, len(l) - 1
        wowels = set('aAeEiIoOuU')
        while left < right:
            while left < right and l[left] not in wowels:
                left += 1
            while right >= 0 and l[right] not in wowels:
                right -= 1
            if left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        return ''.join(l)


if __name__ == '__main__':
    sl = Solution()

    ret = sl.reverseVowels("a.b,.")
    print(ret)
