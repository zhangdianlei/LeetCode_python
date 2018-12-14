# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/13 5:15 PM
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    if numRows == 0:
        return []

    result = [[1]]

    for i in range(1, numRows+1):
        temp = []
        for j in range(i):
            if j == 0 or j == i - 1:
                temp.append(1)
            else:
                temp.append(result[i-1][j-1] + result[i-1][j])

        result.append(temp)
    result.pop(0)
    return result


if __name__ == '__main__':
    n = 5

    print(generate(5))
