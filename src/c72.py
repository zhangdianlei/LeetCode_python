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

    arr = m * [[0] * n]

    pointer = 0
    for i in range(m):
        arr[i][0] = pointer
        pointer += 1

    # for i in range(n):
    #     arr[0][i] = i

    print(arr)


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1, word2))
