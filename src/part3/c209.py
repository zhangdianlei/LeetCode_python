# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/8 3:48 PM
"""


def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    if l == 0:
        return 0
    if nums[0] > s:
        return 1
    if sum(nums) < s:
        return 0

    start = 0
    end = 1
    result = l
    while end <= l:

        temp = sum(nums[start:end])
        if temp >= s:
            result = min(result, end - start)
            while temp >= s:
                result = min(result, end - start)
                start = start + 1
                temp = sum(nums[start:end])
        else:
            end = end + 1

    return result


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(s, nums))
