# coding:utf-8

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/ (83. Remove Duplicates from Sorted List)

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        q = p.next
        while q:
            if q.val == p.val:
                p.next = q.next
                q = p.next
            else:
                p = q
                q = q.next

        return head


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    exe = Solution()
    head = exe.deleteDuplicates(head)
    p = head
    while p:
        print p.val
        p = p.next
