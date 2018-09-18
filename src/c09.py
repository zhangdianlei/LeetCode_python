# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/17 16:55
@python version: 

"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)

        if s == s[::-1]:
            return True
        else:
            return False


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
            x = int(line);

            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()