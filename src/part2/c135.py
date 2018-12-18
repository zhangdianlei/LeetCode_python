# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/18 7:13 PM
"""


def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    if not ratings:
        return 0

    nums = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            nums[i] = nums[i - 1] + 1

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and nums[i] < nums[i + 1] + 1:
            nums[i] = nums[i + 1] + 1

    result = 0
    for i in nums:
        result += i

    return result


if __name__ == '__main__':
    ratings = [1, 2, 87, 87, 87, 2, 1]

    print(candy(ratings))
