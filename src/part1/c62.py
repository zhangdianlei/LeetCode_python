# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/18 17:24
@python version: 

"""


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    matrix = []
    for i in range(m):
        matrix.append([0] * n)

    matrix[0] = [1] * n
    for i in range(m):
        matrix[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[m - 1][n - 1]


if __name__ == '__main__':
    m = 1
    n = 1
    print(uniquePaths(m, n))
