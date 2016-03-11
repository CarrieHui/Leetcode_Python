# coding:utf-8

# https://leetcode.com/problems/plus-one/ (66. Plus One)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 0
        for i in range(length-1, -1, -1):
            if i == length - 1 :
                s = digits[i] + 1
            else:
                s = digits[i] + carry

            if s == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = s
                carry = 0
                break

        if carry == 1:
            digits.insert(0,1)

        return digits


if __name__ == '__main__':
    exe = Solution()
    new_digidts = exe.plusOne([1,9,9])
    print new_digidts