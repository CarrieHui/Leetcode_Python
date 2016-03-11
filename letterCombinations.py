# coding:utf-8

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/ (17. Letter Combinations of a Phone Number)

class Solution(object):
    def reCombination(self, map, num, digits, length, res, result):
    # map为映射表, num为遍历到digits中的第num个位置, length为digits的长度, res为当前的一个结果字符串(未完成的), result的最终的结果列表
        for i in map[digits[num]]:
            # res += i
            if(num < length-1):
                self.reCombination(map, num+1, digits, length, res+i, result)
            if(num == length-1):
                result.append(res+i)
            # res = res[0: len(res)-1]


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        result = []
        if length == 0:
            return result
        map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ''
        self.reCombination(map, 0, digits, length, res, result)
        return result


if __name__ == '__main__':
    exe = Solution()
    print exe.letterCombinations('234')
