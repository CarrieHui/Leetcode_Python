# coding:utf-8

# https://leetcode.com/problems/reverse-linked-list-ii/ (92. Reverse Linked List II)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dif = n - m
        if head == None or head.next == None or dif==0:
            return head
        super_head = ListNode(0)
        super_head.next = head
        w = super_head
        while m > 1:
            w = w.next
            m -= 1

        p1 = w.next
        p2 = p1.next
        p3 = p2.next
        while True:
            p2.next = p1
            dif -= 1
            if dif == 0:
                break
            p1 = p2
            p2 = p3
            p3 = p3.next
        w.next.next = p3
        w.next = p2

        return super_head.next


if __name__ == '__main__':

    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node5 = ListNode(6)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    exe = Solution()
    p = exe.reverseBetween(head, 1, 6)
    while p:
        print str(p.val)
        p = p.next
