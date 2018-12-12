# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/22 13:52
@python version: 

"""

def p(n):
    if n == 2:
        return 2
    if n == 3:
        return 3
    return p(n - 1) + p(n - 2)


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    result = p(n - 1) + p(n - 2)
    return result


if __name__ == '__main__':
    n = 2
    print(climbStairs(n))
