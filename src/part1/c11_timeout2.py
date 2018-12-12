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

        a = sorted(height)
        index_arra = []

        for item in a:
            temp = height.index(item)
            index_arra.append(temp)
            height[temp] = -1

        result = 0
        for index, item in enumerate(a):

            if index <= len(a)-2:

                min_index = min(index_arra[index + 1:])
                max_index = max(index_arra[index + 1:])

                temp = abs(index_arra[index] - min_index)
                if abs(index_arra[index] - max_index) > temp:
                    temp = abs(index_arra[index] - max_index)

                current_result = temp * item

                if current_result > result:
                    result = current_result

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

