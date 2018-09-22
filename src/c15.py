# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/22 17:03
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

        nums = sorted(nums)

        for index, item in enumerate(nums):

            target = -item
            start = index + 1
            end = len(nums) - 1

            if item > 0 or nums[end] < 0:
                break

            if index > 0 and item == nums[index-1]:
                continue

            while start < end:

                if nums[end] < 0:
                    break

                if nums[start] + nums[end] == target:
                    temp_list = [nums[index], nums[start], nums[end]]
                    result.append(temp_list)

                    while start < end and nums[start] == nums[start+1]:
                        start = start + 1
                    while start < end and nums[end] == nums[end-1]:
                        end = end - 1

                    start = start + 1
                    end = end - 1

                elif nums[start] + nums[end] < target:
                    start = start + 1

                else:
                    end = end - 1

        return result


if __name__ == '__main__':
    # nums = [0, 0, 0]
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    so = Solution()
    print(so.threeSum(nums))
