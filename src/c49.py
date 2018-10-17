# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/17 15:41
@python version: 

"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    result = {}

    for i in strs:
        temp = ''.join(sorted(i))
        if temp in result.keys():
            result[temp].append(i)
        else:
            result[temp] = []
            result[temp].append(i)

    final = []

    for value in result.values():
        final.append(value)

    return final


if __name__ == '__main__':
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["eat", "t"]
    print(groupAnagrams(strs))
