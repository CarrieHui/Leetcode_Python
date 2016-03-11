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
        q = []  # queue
        ret = []
        if root == None:
            return ret
        q.append(root)
        current = 1
        next = 0

        while q:
            ret.append(q[-1].val)
            while current > 0:
                if q[0].left != None:
                    q.append(q[0].left)
                    next += 1
                if q[0].right != None:
                    q.append(q[0].right)
                    next += 1
                del q[0]
                current -= 1
            current = next
            next = 0

        return  ret


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