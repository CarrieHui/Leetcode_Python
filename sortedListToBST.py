# coding:utf-8

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/ (109. Convert Sorted List to Binary Search Tree)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    curNode = None  # 类属性

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        size = 0
        p = head
        self.curNode = head  # 为类属性赋值
        while p:
            size += 1
            p = p.next

        return self.genTree(0, size-1)


    def genTree(self, begin, end):
        if begin > end:
            return None

        mid = int((begin + end) / 2)
        left = self.genTree(begin, mid-1)
        treeNode = TreeNode(self.curNode.val)
        self.curNode = self.curNode.next
        treeNode.left = left

        right = self.genTree(mid+1, end)
        treeNode.right = right

        return treeNode


def printTree(node):
    if node == None:
        print '#'
        return
    else:
        print node.val
        printTree(node.left)
        printTree(node.right)

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

    exe = Solution()
    tree = exe.sortedListToBST(head)
    printTree(tree)
