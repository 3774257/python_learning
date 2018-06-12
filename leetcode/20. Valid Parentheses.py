"""https://leetcode.com/problems/valid-parentheses/description/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stacks = [' ']
        d_left = {'{': '}', '[': ']', '(': ')'}

        for c in s:
            if c in '([{':
                stacks.append(c)
            else:
                if d_left.get(stacks.pop(), '') != c:
                    return False
        return True if stacks == [' '] else False
