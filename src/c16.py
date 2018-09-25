# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/25 15:14
@python version: 

"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = [-1, 2, 1, -4]
        target = 1

        nums = sorted(nums)
        length = len(nums)
        distance = abs(nums[length - 1] + nums[length - 2] + nums[length - 3] - target)
        result = nums[length - 1] + nums[length - 2] + nums[length - 3]

        if distance < abs(nums[0] + nums[1] + nums[2] - target):
            distance = abs(nums[0] + nums[1] + nums[2] - target)
            result = nums[0] + nums[1] + nums[2]

        for index, item in enumerate(nums):

            temp = target - item
            start = index + 1
            end = length - 1

            while start < end:

                diff = nums[start] + nums[end] - temp
                current = item + nums[start] + nums[end]
                if abs(diff) < distance:
                    distance = abs(diff)
                    result = current

                if diff > 0:
                    end = end - 1
                elif diff == 0:
                    return item + nums[start] + nums[end]
                else:
                    start = start + 1

        return result


def stringToIntegerList(input):
    return list(map(int, input))


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

            ret = Solution().threeSumClosest(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
