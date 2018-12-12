# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/17 16:15
@python version: 

"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    result = nums[0]
    temp = nums[0]
    for i in range(1, len(nums)):
        if temp + nums[i] > 0:
            temp = temp + nums[i]

            if temp < nums[i]:
                temp = nums[i]

            if temp > result:
                result = temp
        elif nums[i] >= 0:
            temp = nums[i]
            if nums[i] > result:
                result = nums[i]
        else:
            temp = 0
            if nums[i] > result:
                result = nums[i]

    return result


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
