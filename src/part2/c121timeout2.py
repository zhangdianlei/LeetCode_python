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

    result = []
    for i in range(length):
        result.append(max(prices[i:]) - prices[i])

    return max(result)


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]

    print(maxProfit(prices))
