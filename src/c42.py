# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/12 15:54
@python version: 

"""


def findLeft(height, h):
    """
    :param height:
    :param h:
    :return: first left index
    """
    for index, item in enumerate(height):
        if item >= h:
            return index


def findRight(height, h):
    """
    :param height:
    :param h:
    :return: first right index
    """
    i = len(height) - 1
    while i >= 0:
        if height[i] >= h:
            return i
        i = i - 1


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    sortHeight = sorted(height)

    if len(height) == 1:
        return 0

    pre = 0
    next = 0
    result = 0
    for h in sortHeight:
        if h == next:
            continue
        elif h > next:
            pre = next
            next = h
            left = findLeft(height, next)
            right = findRight(height, next)
            result = result + (next - pre) * (right - left + 1)

    return result - sum(height)


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    print(trap(height))
