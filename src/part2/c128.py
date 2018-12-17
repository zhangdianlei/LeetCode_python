# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/17 3:04 PM
"""


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    d = {}
    ans = 0
    for i in nums:
        if i not in d:
            left = d.get(i - 1, 0)
            right = d.get(i + 1, 0)
            length = left + right + 1
            ans = max(ans, length)

            d[i] = length
            d[i - left] = length
            d[i + right] = length

    return ans


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2, 3]

    print(longestConsecutive(nums))
