# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/10 13:51
@python version: 

"""
import json


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = [1]
        start = 0
        end = len(nums) - 1

        if target < nums[start]:
            return start
        if target > nums[end]:
            return end + 1

        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0

        while start < end:

            if start + 1 == end:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                return start + 1

            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid


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
            line = next(lines)
            target = int(line);

            ret = Solution().searchInsert(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
