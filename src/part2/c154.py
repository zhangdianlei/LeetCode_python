# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2018/12/26 4:44 PM
"""


def findMin(nums, init):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]

    result = init
    if nums[0] <= nums[-1]:
        if nums[0] <= result:
            result = nums[0]
    else:
        result = min(findMin(nums[0:len(nums) // 2], result), findMin(nums[len(nums) // 2:], result), result)

    return result


if __name__ == '__main__':
    # nums = [2, 2, 2, 0, 1]
    nums = [3, 1, 3]
    nums = [1, 3, 5]
    nums = [1, 1, 1]

    pre = nums[0]
    new = [pre]
    for i in range(1, len(nums)):
        if nums[i] != pre:
            new.append(nums[i])
            pre = nums[i]

    if len(new) > 1:
        if new[0] == new[-1]:
            new = new[1:]
    else:
        # return nums[0]
        print(nums[0])

    print(findMin(new, 99999999))
