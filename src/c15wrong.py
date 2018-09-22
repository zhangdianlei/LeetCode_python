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

        start = 0
        end = len(nums) - 1
        nums = sorted(nums)

        while start < end:
            sum = nums[start] + nums[end]
            if -sum in nums[start + 1:end]:
                temp = sorted([nums[start], nums[end], -sum])
                if temp not in result:
                    result.append(temp)

            if sum > 0:
                end = end - 1

            elif sum == 0:
                temp_value = -nums[start]

                a = start + 1
                b = end - 1
                if b - a > 0:
                    while a < b:
                        if nums[a] + nums[b] < temp_value:
                            a = a + 1
                        elif nums[a] + nums[b] == temp_value:
                            temp_list = sorted([nums[a], nums[b], nums[start]])
                            if temp_list not in result:
                                result.append(temp_list)
                            a = a + 1
                        else:
                            b = b - 1

                start = start + 1
            else:
                start = start + 1

        return result


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    so = Solution()
    print(so.threeSum(nums))
