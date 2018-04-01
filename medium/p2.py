# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0)
        head = prev
        carrier = ListNode(0)
        while(l1 is not None or l2 is not None or carrier.val != 0):
            # finish the boundary
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            sum = l1.val + l2.val + carrier.val
            carrier.val = sum // 10
            prev.next = ListNode(sum % 10)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next

        return head.next


