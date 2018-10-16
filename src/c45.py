# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/15 16:39
@python version: 

"""


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last = len(nums) - 1
    step = 0
    index = 0

    if len(nums) == 1:
        return 0

    while index + nums[index] < last:
        step = step + 1

        max = 0
        maxIndex = 0
        for i in range(1, nums[index] + 1):
            temp = i + index
            if temp + nums[temp] >= max:
                max = temp + nums[temp]
                maxIndex = temp

        index = maxIndex

    return step + 1


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 3, 1, 1, 4]
    nums = [1, 2, 3]
    print(jump(nums))
