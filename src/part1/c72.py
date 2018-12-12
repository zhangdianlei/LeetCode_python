# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/22 17:14
@python version: 

"""


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1) + 1
    n = len(word2) + 1

    arr = [[0] * n for i in range(m)]

    row = [i for i in range(n)]
    arr[0] = row
    for i in range(m):
        arr[i][0] = i

    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                arr[i + 1][j + 1] = arr[i][j]
            else:
                arr[i + 1][j + 1] = min(arr[i][j + 1], arr[i + 1][j], arr[i][j]) + 1

    return arr[m - 1][n - 1]


if __name__ == '__main__':
    word1 = "ros"
    word2 = "horse"
    print(minDistance(word1, word2))
