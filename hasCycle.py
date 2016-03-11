# coding:utf-8

# https://leetcode.com/problems/linked-list-cycle/ (141. Linked List Cycle)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        if head == None or head.next == None:
            return False
        p = head
        q = head.next
        while p and q:
            if p == q:
                return True
            else:
                p = p.next
                q = q.next
                if q:
                    q = q.next
                else:
                    return False
        return False
        '''

        if head == None or head.next == None:
            return False
        p = head
        q = head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False


if __name__ == '__main__':
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node2

    exe = Solution()
    print exe.hasCycle(head)