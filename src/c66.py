# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/22 13:39
@python version: 

"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    print(digits)

    num = int(''.join([str(t) for t in digits])) + 1

    return [int(i) for i in str(num)]


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(plusOne(digits))
