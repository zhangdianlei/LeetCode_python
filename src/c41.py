# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/12 15:10
@python version: 

"""
import json


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0, 2, 2, 1, 1]
        nums = sorted(nums)

        data = 0
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] - data > 1:
                return data + 1
            elif nums[i] > 0:
                data = nums[i]

        return data + 1


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
            nums = stringToIntegerList(line);

            ret = Solution().firstMissingPositive(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
