# coding:utf-8

# https://leetcode.com/problems/binary-search-tree-iterator/ (173. Binary Search Tree Iterator)

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        tmp = self.stack.pop()
        self.pushAll(tmp.right)
        return tmp.val

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left


if __name__ == '__main__':

    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(8)
    root.left = node1
    root.right = node2
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node1.left = node3
    node1.right = node4

    i = BSTIterator(root)
    v = []
    while i.hasNext():
        v.append(i.next())
    print v
