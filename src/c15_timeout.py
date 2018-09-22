# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/21 15:42
@python version: 

"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        result = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if -sum in nums:
                    k = nums.index(-sum)
                    if k != i and k != j:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        if temp not in result:
                            result.append(temp)

        return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    so = Solution()
    print(so.threeSum(nums))
