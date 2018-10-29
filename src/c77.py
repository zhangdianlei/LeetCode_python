# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/29 15:53
@python version: 

"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.count = 0

        def dfs(start, nums):

            if self.count == k:
                ans.append(nums)
                return

            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, nums + [i])
                self.count -= 1

        dfs(1, [])

        return ans


if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution.combine(Solution, n, k))
