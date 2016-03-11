# coding:utf-8

# https://leetcode.com/problems/binary-tree-right-side-view/ (199. Binary Tree Right Side View)

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.recurTraversal(1, root, ret)
        return  ret


    def recurTraversal(self, level, node, ret):
        if node == None:
            return
        if(len(ret) < level):
            ret.append(node.val)
        self.recurTraversal(level+1, node.right, ret)
        self.recurTraversal(level+1, node.left, ret)


if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.left = node1
    root.right = node2
    node1.left = node3
    node3.right = node4
    exe = Solution()
    print exe.rightSideView(root)