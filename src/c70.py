# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/22 14:07
@python version: 

"""

def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    return list(Fibonacci_Yield_tool(n+1))[-1]


if __name__ == '__main__':
    print(climbStairs(5))
