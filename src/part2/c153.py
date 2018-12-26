# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/26 4:44 PM
"""


def findMin(nums, init):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = init
    if nums[0] <= nums[-1]:
        if nums[0] <= result:
            result = nums[0]
    else:
        result = min(findMin(nums[0:len(nums) // 2], result), findMin(nums[len(nums) // 2:], result), result)

    return result


if __name__ == '__main__':
    nums = [4, 5, 6, 7, -3, -2, 0, 1, 2]

    print(findMin(nums, 99999999))
