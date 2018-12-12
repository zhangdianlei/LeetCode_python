# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/23 16:20
@python version: 

"""


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = [0, 0, 0]
    for index, item in enumerate(nums):
        if item == 0:
            count[0] += 1
        if item == 1:
            count[1] += 1
        if item == 2:
            count[2] += 1

    pointer = 0
    for index, length in enumerate(count):
        for j in range(length):
            nums[pointer] = index
            pointer += 1

    return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums))
