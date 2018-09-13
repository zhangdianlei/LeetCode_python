# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/12 08:29
@python version: 

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for index, item in enumerate(nums):

            for i in range(index, len(nums)):

                if item + nums[i] == target:
                    result.append(index)
                    result.append(i)
                    return result


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    so = Solution()
    print(so.twoSum(nums, target))
