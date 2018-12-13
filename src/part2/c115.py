# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/13 3:20 PM
"""


def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    col = len(s)
    row = len(t)

    if row > col:
        return 0

    matrix = []

    for i in range(row):
        matrix.append([0] * col)

    # 初始化矩阵
    for i in range(row):
        for j in range(col):
            if t[i] == s[j]:
                matrix[i][j] = "X"

    # 初始化第一行
    for j in range(col):
        if matrix[0][j] == "X":
            matrix[0][j] = 1

    # 初始化第一列
    for i in range(row):
        if matrix[i][0] == "X":
            matrix[i][0] = 0

    # 计算矩阵中的值
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == "X":
                matrix[i][j] = sum(matrix[i - 1][0:j])

    return sum(matrix[row-1])


if __name__ == '__main__':
    # S = "rabbbit"
    # T = "rabbit"

    S = "babgbag"
    T = "bag"

    print(numDistinct(S, T))
