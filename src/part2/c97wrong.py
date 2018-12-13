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
    s1Set = set()
    pointer = 0

    for index, item in enumerate(s1):
        if s3.find(item, pointer) != -1:
            s1Set.add(s3.find(item, pointer))
            pointer = s3.find(item, pointer) + 1
        else:
            return False

    print('s1Set', s1Set)
    s2_temp = ""
    for index, item in enumerate(s3):
        if index not in s1Set:
            s2_temp += item

    if s2_temp == s2:
        return True
    else:
        return False


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    print(isInterleave(s1, s2, s3))
