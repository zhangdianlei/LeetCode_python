# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/14 3:31 PM
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1:
        return 0

    result = 0
    for i in range(len(prices)-1):
        result += max(prices[i + 1] - prices[i], 0)

    return result


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]

    print(maxProfit(prices))
