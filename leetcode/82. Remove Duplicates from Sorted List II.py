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
        rets = ListNode(None)
        prenode = ltmp = rets
        precnts = -1
        j = head
        while j:
            if j.val == prenode.val:
                precnts += 1
            else:
                if precnts == 1:
                    ltmp.next = prenode
                    ltmp = ltmp.next
                prenode = j
                precnts = 1
            j = j.next
        if precnts == 1:
            ltmp.next = prenode
            ltmp = ltmp.next
        ltmp.next = None
        return rets.next
