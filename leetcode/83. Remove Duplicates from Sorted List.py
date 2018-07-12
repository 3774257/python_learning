# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        tmp = ret
        t = head

        while t:
            if t.val != tmp.val:
                tmp.next = t
                tmp = t
            t = t.next
        tmp.next = None
        return ret.next
