# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/16 16:55
@python version: 

"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    if len(nums) == 0:
        return result

    first = [nums[0]]
    result.append(first)

    for i in range(1, len(nums)):
        number = nums[i]

        while len(result[0]) == i:
            temp = result.pop(0)

            for j in range(len(temp) + 1):
                temp.insert(j, number)
                result.append(temp[:])
                temp.remove(number)

    return result


if __name__ == '__main__':
    nums = [1, 1, 2, 4]
    print(permute(nums))
