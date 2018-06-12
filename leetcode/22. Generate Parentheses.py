class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.rets = []
        self.n = n
        left = right = 0
        curs = ''
        self.subgenerate(curs + '(', left + 1, right)
        return self.rets

    def subgenerate(self, curs, left, right):
        # 递归法求解，符合条件添加结果
        if left == right == self.n:
            self.rets.append(curs)
            return
        # 还可加左括号就加
        if left < self.n:
            self.subgenerate(curs + '(', left + 1, right)
        # 还可加右括号就加
        if left > right < self.n:
            self.subgenerate(curs + ')', left, right + 1)

