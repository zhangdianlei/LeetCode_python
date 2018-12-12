# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/18 16:52
@python version: 

"""


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    a = s.split(" ")
    a.reverse()
    for i in a:
        if len(i) > 0:
            return len(i)
    return 0


if __name__ == '__main__':
    # s = "Hello World"
    s = "Hello World "
    # s = ""
    print(lengthOfLastWord(s))
