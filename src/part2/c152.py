# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/24 5:26 PM
"""


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    B = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(max(nums), max(B))


if __name__ == '__main__':
    nums = [2, 3, -2, 4]

    print(maxProduct(nums))
