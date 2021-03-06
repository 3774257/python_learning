"""
https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmpres = res = ListNode(0)
        carry = 0
        while l1 and l2:
            carry += l1.val + l2.val
            carry, t = divmod(carry, 10)
            tmpres.next = ListNode(t)
            tmpres = tmpres.next
            l1 = l1.next
            l2 = l2.next
        left = l1 or l2
        while left:
            carry += left.val
            carry, t = divmod(carry, 10)
            tmpres.next = ListNode(t)
            tmpres = tmpres.next
            left = left.next
        if carry:
            tmpres.next = ListNode(carry)
        return res.next
