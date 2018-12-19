# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/19 2:33 PM
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for i in nums:
        result ^= i

    return result


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2, 5, 5]
    nums = [1]
    print(singleNumber(nums))
