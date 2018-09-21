# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/21 10:56
@python version: 

"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""

        first = strs[0]
        common = ""
        if len(first) > 0:
            for i in range(0, len(first) + 1):
                str = first[0:i]
                for item in strs:
                    if item.startswith(str) is False:
                        return common
                common = str

            return common
        else:
            return common


if __name__ == '__main__':
    # strs = ["flower", "flow", "flight"]
    strs = ["c","racecar","car"]
    so = Solution()
    print(so.longestCommonPrefix(strs))
