class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return list(s)"""

        x = a = b = 0

        for n in nums:
            x ^= n
        mask = 1
        while not (x & mask):
            mask <<= 1
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n
        return [a, b]