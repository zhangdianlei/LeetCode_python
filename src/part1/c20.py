# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/26 17:01
@python version: 

"""
import json


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        stack = []

        for item in s:
            if item == '[' or item == '(' or item == '{':
                stack.append(item)

            if item == ']':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '[':
                    return False

            if item == ')':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '(':
                    return False

            if item == '}':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '{':
                    return False

        if len(stack) > 0:
            return False
        else:
            return True


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
            s = str(line)

            ret = Solution().isValid(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
