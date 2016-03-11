# coding:utf-8

# https://leetcode.com/problems/combination-sum/ (39. Combination Sum)


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        end = len(candidates) - 1
        while end >= 0 and candidates[end] > target:
            end -= 1
        self.recurCombine(candidates[:end+1], target, result, [])
        return result


    def recurCombine(self, candidates, target, result, temp):
        if target == 0:
            result.append(temp)
            return
        elif candidates == []:
            return
        else:
            for i in range(0, len(candidates)):
                end = len(candidates) - 1
                while end >= 0 and candidates[end] > target-candidates[i]:
                    end -= 1
                self.recurCombine(candidates[i:end+1], target-candidates[i], result, temp+[candidates[i]])


if __name__ == '__main__':
    exe = Solution()
    result = exe.combinationSum([1, 2, 3, 6, 7], 7)
    print result
