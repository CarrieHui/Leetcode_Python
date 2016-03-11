# coding:utf-8

# https://leetcode.com/problems/unique-paths/ (62. Unique Paths)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.continueProduct(m,m+n-2)/self.continueProduct(1,n-1)

    def continueProduct(self, begin, end):
        ret = 1
        for i in range(begin, end+1):
            ret *= i
        return ret


if __name__ == '__main__':
    exe = Solution()
    print exe.uniquePaths(1, 2)