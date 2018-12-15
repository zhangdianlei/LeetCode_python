# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/14 3:39 PM
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if len(prices) < 2:
        return 0

    result = []
    for i in range(len(prices) - 1):
        result.append(prices[i + 1] - prices[i])

    merge_result = [0, 0]
    for i in range(len(result)):
        if result[i] >= 0:
            merge_result[-1] += result[i]
        else:
            temp = merge_result[-1] + result[i]
            if temp > 0:
                merge_result.append(temp)
            else:
                merge_result.append(0)

    one = max(merge_result)
    merge_result.pop(merge_result.index(one))
    two = max(merge_result)

    return one + two


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [1, 2, 3, 4, 5]
    prices = [7, 6, 4, 3, 1]
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]

    print(maxProfit(prices))
