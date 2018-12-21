# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/21 3:53 PM
"""


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    if not s:
        return True

    breakp = [0]

    for i in range(len(s) + 1):
        for j in breakp:
            if s[j:i] in wordDict:
                breakp.append(i)
                break
    return breakp[-1] == len(s)


if __name__ == '__main__':
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    s = "catsanddog"
    wordDict = ["cats", "and", "cat", "dog"]

    print(wordBreak(s, wordDict))
