# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/9 3:23 PM
"""


def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for i in nums:
        index = abs(i) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            result.append(abs(index+1))

    return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1, 1]
    print(findDuplicates(nums))
