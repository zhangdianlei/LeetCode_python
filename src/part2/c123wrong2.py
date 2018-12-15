# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/15 2:15 PM
"""


def getMaxOne(prices):
    length = len(prices)

    if length == 0:
        return [0, 0, 0]

    min_p, max_p = 99999999, 0
    min_index, max_index = 0, 0

    for index, item in enumerate(prices):
        if item < min_p:
            min_p = item
            min_index = index
        if item - min_p > max_p:
            max_p = item - min_p
            max_index = index

    return [max_p, min_index, max_index]


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1:
        return 0

    one = getMaxOne(prices)

    pre = [0, 0, 0]
    if one[1] < one[2]:
        pre = getMaxOne(prices[0:one[1]])

    tail = [0, 0, 0]
    cut = []
    if one[2] + 1 < len(prices):
        tail = getMaxOne(prices[one[2] + 1:])

        if one[1] > one[2]:
            cut = prices[0:one[1]]
        else:
            cut = prices[one[1]:one[2] + 1]
    else:
        cut = prices[one[1]:]

    dis = 0
    temp = 0
    if len(cut) > 2:
        for i in range(1, len(cut) - 1):
            if cut[i] - cut[i - 1] < temp:
                temp += cut[i] - cut[i - 1]
                dis = min(dis, temp)
            else:
                temp = 0

    result = max(one[0] - dis, one[0] + pre[0], one[0] + tail[0])
    return result


if __name__ == '__main__':
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # prices = [7, 6, 4, 3, 1]
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    # prices = [1, 2, 3, 4, 5]
    # prices = [2, 4, 1]
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]

    print(maxProfit(prices))
