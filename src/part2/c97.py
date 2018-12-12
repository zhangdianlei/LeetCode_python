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
    s1Arr = []
    pointer = 0

    for index, item in enumerate(s1):
        if s3.find(item, pointer) != -1:
            s1Arr.append(s3.find(item, pointer))
        else:
            return False
        pointer = index + 1

    print('s1arr', s1Arr)


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    isInterleave(s1, s2, s3)
