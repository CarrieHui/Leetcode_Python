# coding: utf-8

# https://leetcode.com/problems/valid-anagram/ (242. Valid Anagram)

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alph = [];
        for i in range(0, 64):
            alph.append(0)
        for i in s:
            alph[ord(i)-ord('a')] += 1;
        for i in t:
            alph[ord(i)-ord('a')] -= 1;
        for i in range(0, 64):
            if alph[i] != 0:
                return False
        return True

if __name__ == '__main__':
    print isAnagram('cat', 'tact')
