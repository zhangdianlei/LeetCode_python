# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/21 08:19
@python version: 

"""
import json


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

        max = 0
        temp_y = 0
        for i in range(len(height)-1):

            if height[i] <= temp_y:
                continue
            else:
                temp_y = height[i]

            for j in range(i+1, len(height)):
                x = j - i

                y = height[i]
                if height[j] < height[i]:
                    y = height[j]
                temp = x * y
                if temp > max:
                    max = temp

        return max


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            height = stringToIntegerList(line);

            ret = Solution().maxArea(height)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

