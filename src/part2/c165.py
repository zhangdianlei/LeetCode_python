# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/28 10:02 AM
"""


def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split('.')
    v2 = version2.split('.')

    length = min(len(v1), len(v2))

    for i in range(length):
        if int(v1[i]) > int(v2[i]):
            return 1
        if int(v1[i]) < int(v2[i]):
            return -1

    if len(v1) > len(v2):
        for i in range(len(v2), len(v1)):
            if int(v1[i]) != 0:
                return 1
        return 0
    elif len(v1) == len(v2):
        return 0
    else:
        for i in range(len(v1), len(v2)):
            if int(v2[i]) != 0:
                return -1
        return 0


if __name__ == '__main__':
    version1 = "7.5.3.5.0.1"
    version2 = "7.5.3.5"

    print(compareVersion(version1, version2))
