# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/19 2:55 PM
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    one = two = 0  # 记录数组中出现一次和两次的异或，出现三次会在出现一次中消去
    for n in nums:
        one = ~two & (one ^ n)
        two = ~one & (two ^ n)
    return one


if __name__ == '__main__':
    nums = [5, 5, 5, 2, 3, 2, 3, 2, 3, 99]
    print(singleNumber(nums))
