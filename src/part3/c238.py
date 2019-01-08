# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/8 4:50 PM
"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    size = len(nums)
    tmp = 1
    result = [1]
    for i in range(1, size):
        tmp *= nums[i - 1]
        result.append(tmp)
    tmp = 1
    for i in range(size - 2, -1, -1):
        tmp *= nums[i + 1]
        result[i] *= tmp
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
