# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/17 16:53
@python version:

"""


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    flag = "right"
    x = y = 0
    m = len(matrix)
    n = len(matrix[0])
    result = []

    while flag != "over":
        result.append(matrix[x][y])
        matrix[x][y] = "X"

        if flag == "right":
            if y + 1 < n:
                if matrix[x][y + 1] != "X":
                    y = y + 1
                    continue
                else:
                    if x + 1 < n:
                        if matrix[x + 1][y] != "X":
                            x = x + 1
                            flag = "down"
                        else:
                            flag = "over"
                    else:
                        flag = "over"
            else:
                if x + 1 < n:
                    if matrix[x + 1][y] != "X":
                        x = x + 1
                        flag = "down"
                    else:
                        flag = "over"
                else:
                    flag = "over"
        if flag == "down":
            if x + 1 < m:
                if matrix[x + 1][y] != "X":
                    x = x + 1
                    continue
                else:
                    if y - 1 >= 0:
                        if matrix[x][y - 1] != "X":
                            y = y - 1
                            flag = "left"
                        else:
                            flag = "over"
                    else:
                        flag = "over"
            else:
                if y - 1 >= 0:
                    if matrix[x][y - 1] != "X":
                        y = y - 1
                        flag = "left"
                    else:
                        flag = "over"
                else:
                    flag = "over"
        if flag == "left":
            if y - 1 >= 0:
                if matrix[x][y - 1] != "X":
                    y = y - 1
                    continue
                else:
                    if x - 1 >= 0:
                        if matrix[x - 1][y] != "X":
                            x = x - 1
                            flag = "up"
                        else:
                            flag = "over"
                    else:
                        flag = "over"
            else:
                if x - 1 >= 0:
                    if matrix[x - 1][y] != "X":
                        x = x - 1
                        flag = "up"
                    else:
                        flag = "over"
                else:
                    flag = "over"
        if flag == "up":
            if x - 1 >= 0:
                if matrix[x - 1][y] != "X":
                    x = x - 1
                    continue
                else:
                    if y + 1 < n:
                        if matrix[x][y + 1] != "X":
                            y = y + 1
                            flag = "right"
                        else:
                            flag = "over"
                    else:
                        flag = "over"
            else:
                if y + 1 < n:
                    if matrix[x][y + 1] != "X":
                        y = y + 1
                        flag = "right"
                    else:
                        flag = "over"
                else:
                    flag = "over"

    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(spiralOrder(matrix))
