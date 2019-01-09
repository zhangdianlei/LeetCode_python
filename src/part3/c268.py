# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/9 2:46 PM
"""


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    arr = [-1] * (l + 1)
    for i in nums:
        arr[i] = i

    for index, j in enumerate(arr):
        if j == -1:
            return index


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # nums = [0]

    print(missingNumber(nums))
