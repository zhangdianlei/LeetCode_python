# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/17 15:53
@python version: 

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(str(x)) == 0:
            return 0
        else:
            s = str(x)
            start = ""
            if s[0:1] == "-":
                s = s[1:]
                start = "-"

            s = s[::-1]
            result = int(start + s)

            if -2 ** 31 <= result <= (2 ** 31 - 1):
                return result
            else:
                return 0


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
            x = int(line)

            ret = Solution().reverse(x)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()