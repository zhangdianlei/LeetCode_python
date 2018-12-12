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

    while last > 0:

        for i in range(last):
            if nums[i] >= (last - i):
                step = step + 1
                last = i
                break

    return step


if __name__ == '__main__':
    nums = [2, 1]
    print(jump(nums))
