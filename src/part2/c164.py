# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/28 9:50 AM
"""


def maximumGap(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)

    result = 0
    if len(nums) < 2:
        return result

    for i in range(len(nums) - 1):
        temp = nums[i + 1] - nums[i]
        if temp > result:
            result = temp

    return result


if __name__ == '__main__':
    nums = [3, 6, 9, 1]
    print(maximumGap(nums))
