# coding:utf-8

# https://leetcode.com/problems/intersection-of-two-linked-lists/ (160. Intersection of Two Linked Lists)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = 0, 0
        p = headA
        q = headB
        while p:
            a += 1
            p = p.next
        while q:
            b += 1
            q = q.next

        p =headA
        q =headB

        if a > b:
            dif = a - b
            while dif > 0:
                p = p.next
                dif -= 1

        elif b > a:
            dif = b - a
            while dif > 0:
                q = q.next
                dif -= 1

        while p:
            if p == q:
                return p
            p = p.next
            q = q.next

        return None


if __name__ == '__main__':
     head1 = ListNode('a1')
     head2 = ListNode('b1')
     node1 = ListNode('a2')
     node2 = ListNode('b2')
     node3 = ListNode('b3')
     node4 = ListNode('c1')
     node5 = ListNode('c2')
     node6 = ListNode('c3')

     head1.next = node1
     node1.next = node4
     node4.next = node5
     node5.next = node6
     head2.next = node2
     node2.next = node3
     node3.next = node4

     exe = Solution()
     print exe.getIntersectionNode(head1, head2).val
