# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/28 10:30 AM
"""


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start = 0
    end = len(numbers) - 1

    while start < end:
        result = numbers[start] + numbers[end]
        if result == target:
            return [start+1, end+1]
        elif result > target:
            end = end - 1
        else:
            start = start + 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9

    print(twoSum(numbers, target))
