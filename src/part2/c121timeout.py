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

    matrix = []
    for i in range(length):
        matrix.append([0] * length)

    for i in range(length):
        for j in range(i, length):
            matrix[i][j] = prices[j] - prices[i]

    result = []
    for m in range(length):
        result.append(max(matrix[m]))

    return max(result)


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]

    print(maxProfit(prices))
