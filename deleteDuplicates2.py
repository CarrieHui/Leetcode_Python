# coding:utf-8

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ (82. Remove Duplicates from Sorted List II)

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
        super_head = ListNode(0)
        super_head.next = head
        p1 = super_head
        p2 = head
        p3 = p2.next
        while p3:
            if p2.val == p3.val:
                p2 = p3
                p3 = p2.next
            else:
                if p1.next == p2: # 无重复
                    p1 = p2
                    p2 = p3
                    p3 = p3.next  # 有重复
                else:
                    p1.next = p3
                    p2 = p3
                    p3 = p3.next
        if p1.next != p2:
            p1.next = p3
        return super_head.next


if __name__ == '__main__':
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    exe = Solution()
    head = exe.deleteDuplicates(head)
    p = head
    while p:
        print p.val
        p = p.next
