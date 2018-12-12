# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/14 13:10
@python version: 

"""


def judge(str):
    mean = int((len(str) + 1) / 2)

    for i in range(mean):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True


def judge2(str):

    s2 = str[::-1]
    if s2 == str:
        return True
    else:
        return False


class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        if len(s) == 0:
            return result
        else:
            length = 0

            for index, item in enumerate(s):

                endIndex = s.rfind(item)

                while endIndex != -1:
                    tempStr = s[index:endIndex + 1]

                    if judge2(tempStr):

                        if (endIndex - index + 1) > length:
                            length = endIndex - index + 1
                            result = s[index:endIndex + 1]

                            if length >= len(s) - index:
                                return result
                            break

                    endIndex = s.rfind(item, 0, endIndex)

                if endIndex == -1:
                    if length == 0:
                        result = item
                        length = 1

            return result


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
