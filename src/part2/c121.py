# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/14 2:36 PM
"""


def maxProfit(prices):

    length = len(prices)

    if length == 0:
        return 0

    min_p, max_p = 999999, 0
    for i in range(length):
        min_p = min(min_p, prices[i])
        max_p = max(max_p, prices[i] - min_p)

    return max_p


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]

    print(maxProfit(prices))
