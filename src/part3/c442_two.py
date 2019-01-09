# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/9 4:14 PM
"""


def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    l = len(nums) + 1
    result = []
    arr = [0] * l
    for i in nums:
        arr[i] = arr[i] + 1

    for index, j in enumerate(arr):
        if j == 2:
            result.append(index)
    return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1, 1]
    print(findDuplicates(nums))
