# coding:utf-8

# https://leetcode.com/problems/linked-list-cycle-ii/ (142. Linked List Cycle II)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        p = head
        q = head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                p = head
                while True:
                    if p == q:
                        return p
                    else:
                        p = p.next
                        q = q.next
        return None



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
    print exe.hasCycle(head).val