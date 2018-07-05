"""https://leetcode.com/problems/rotate-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        n = 1
        tmp = head
        while tmp.next:
            n += 1
            tmp = tmp.next
        tmp.next = head
        pos = n - (k % n)
        tmp = head
        while pos:
            pre = tmp
            tmp = tmp.next
            pos -= 1
        pre.next = None
        return tmp