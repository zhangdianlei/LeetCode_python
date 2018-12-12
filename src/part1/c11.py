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

        result = 0
        start = 0
        end = len(height)-1

        while start < end:
            x = end - start
            y = min(height[start], height[end])
            result = max(result, x * y)
            if height[start] > height[end]:
                end = end - 1
            else:
                start = start + 1

        return result


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

