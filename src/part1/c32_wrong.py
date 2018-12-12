# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/30 15:17
@python version: 

"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        temp = 0
        stack = []
        for item in s:
            if item == "(":
                stack.append(item)

            else:
                if len(stack) > 0:
                    if stack[-1] == "(":
                        stack.pop()
                        temp = temp + 2
                        if temp > result:
                            result = temp

                    else:
                        stack.append(item)
                        if temp > result:
                            result = temp
                        temp = 0
                else:
                    stack.append(item)
                    if temp > result:
                        result = temp
                    temp = 0
        return result


def stringToString(input):
    return input


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
            s = stringToString(line);

            ret = Solution().longestValidParentheses(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()