# coding : utf-8

# https://leetcode.com/problems/balanced-binary-tree/ (110. Balanced Binary Tree)

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def dfsHeight(self, node):
        if node == None:
            return 0;
        left = self.dfsHeight(node.left)
        right = self.dfsHeight(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        else:
            return max(left, right)+1

    def isBalanced(self, root):
        return self.dfsHeight(root) != -1


root = TreeNode(1);
a = TreeNode(2);
b = TreeNode(3);
c = TreeNode(4);
d = TreeNode(5);
e = TreeNode(6);
root.left = a;
root.right = b;
a.left = c;
b.right = d;
c.left = e;

exe = Solution();
print exe.isBalanced(root)
