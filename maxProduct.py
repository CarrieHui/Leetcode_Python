# coding:utf-8

# https://leetcode.com/problems/maximum-product-of-word-lengths/ (318. Maximum Product of Word Lengths)

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 根据字符串长度对words进行排序
        words.sort(key=len, reverse=True)

        # 字符串列表对应的字母掩码列表
        letters = []
        for i in range(len(words)):
            letters.append(0)
            for j in words[i]:
                letters[i] = letters[i] | (1 << (ord(j)-ord('a')))

        # 求取max的值
        max = 0
        for i in range(len(words)):
            if max > len(words[i] * len(words[i])):
                break;
            for j in range(i+1, len(words)):
                if letters[i] & letters[j] == 0:
                    temp = len(words[i]) * len(words[j])
                    if temp > max:
                        max = temp

        return max



if __name__ == '__main__':
    exe = Solution()
    print exe.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print exe.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
    print exe.maxProduct(["a", "aa", "aaa", "aaaa"])