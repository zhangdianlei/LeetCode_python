# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/14 15:05
@python version: 

"""


class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2 = s[::-1]



def stringToString(input):
    # import json

    return str(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)

            ret = Solution().longestPalindrome(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
