# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/14 2:12 PM
"""


def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    height = len(triangle)
    if height == 0:
        return 0
    if height == 1:
        return triangle[0][0]

    for i in range(height - 2, -1, -1):
        for j in range(i+1):
            triangle[i][j] = min(triangle[i][j] + triangle[i + 1][j], triangle[i][j] + triangle[i + 1][j + 1])

    return triangle[0][0]


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(minimumTotal(triangle))
