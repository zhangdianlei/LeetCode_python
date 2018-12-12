# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/25 16:38
@python version: 

"""
import copy


def back(digits, str, index, result):
    chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if len(digits) == index:
        result.append(str)
        return

    for item in chars[int(digits[index])]:
        back(digits, str+item, index + 1, result)


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        str = ""
        result = []
        index = 0

        if len(digits) == 0:
            return result

        back(digits, str, index, result)

        return result


if __name__ == '__main__':
    digits = "23"
    so = Solution()
    print(so.letterCombinations(digits))
