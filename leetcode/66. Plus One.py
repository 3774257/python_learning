class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        p = 1
        for i in range(len(digits)-1, -1, -1):
            p, digits[i] = divmod(p+digits[i], 10)
        if p:
            digits.insert(0, p)
        return digits
        """
        rets = []
        for n in digits[::-1]:
            p, n = divmod(p+n, 10)
            rets.append(n)
        if p:
            rets.append(p)
        rets.reverse()
        return rets"""
