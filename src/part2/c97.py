# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/12 5:03 PM
"""


def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    if s1 == s2 == s3 == "":
        return True

    if len(s1) + len(s2) != len(s3):
        return False

    # 初始化矩阵
    matrix = []
    for i in range(len(s1) + 1):
        matrix.append([False] * (len(s2) + 1))

    matrix[0][0] = True

    # 初始化边缘
    for i in range(1, len(s1) + 1):
        matrix[i][0] = (matrix[i - 1][0] and (s1[i - 1] == s3[i - 1]))

    for j in range(1, len(s2) + 1):
        matrix[0][j] = (matrix[0][j - 1] and (s2[j - 1] == s3[j - 1]))

    # 循环计算每个节点是否可达
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            top = matrix[i - 1][j] and s1[i - 1] == s3[i - 1 + j]
            left = matrix[i][j - 1] and s2[j - 1] == s3[j - 1 + i]
            matrix[i][j] = top or left

    return matrix[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    print(isInterleave(s1, s2, s3))
