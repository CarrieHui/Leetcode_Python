# coding:utf-8

# https://leetcode.com/problems/sort-colors/ (75. Sort Colors)

class Solution(object):
    def sortColor(self, array):
        low = 0
        high = len(array) - 1
        for i in range(0, len(array)):
            while array[i]== 2 and i<high:
                tmp = array[i]
                array[i] = array[high]
                array[high] = tmp
                high -= 1
            while array[i]==0 and i>low:
                tmp = array[i]
                array[i] = array[low]
                array[low] = tmp
                low += 1

    def sortColor2(self, array):
        white = -1
        red = -1
        blue = -1
        for i in xrange(0, len(array)):
            if array[i] == 0:
                blue += 1
                red += 1
                white += 1
                array[blue] = 2
                array[red] = 1
                array[white] = 0
            elif array[i] == 1:
                blue += 1
                red += 1
                array[blue] = 2
                array[red] = 1
            else:
                blue += 1
                array[blue] = 2


if __name__ == '__main__':
    A = [0, 2, 1 ,0 , 0, 1, 2, 2, 1]
    exe = Solution()
    # exe.sortColor(A)
    exe.sortColor2(A)
    print A