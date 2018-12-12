# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/30 16:14
@python version: 

"""


def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    arr = []
    ans = 0
    for index, item in enumerate(heights):

        if len(arr) == 0:
            arr.insert(0, index)
            continue

        if item > heights[arr[0]]:
            arr.insert(0, index)
        else:
            while heights[arr[0]] >= item:
                top = arr.pop(0)
                if len(arr) == 0:
                    temp = index * heights[top]
                else:
                    temp = (index - arr[0] - 1) * heights[top]

                if temp > ans:
                    ans = temp
                if len(arr) == 0:
                    break

            arr.insert(0, index)

    if len(arr) > 0:
        last = arr[0]

        while len(arr) > 0:
            top = arr.pop(0)

            if len(arr) > 0:
                temp = (last - arr[0]) * heights[top]
                if temp > ans:
                    ans = temp
            else:
                temp = (last + 1) * heights[top]
                if temp > ans:
                    ans = temp

    return ans


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    # heights = [2, 2, 1, 1, 1]
    # heights = [2, 4]
    # heights = [2, 0, 2]
    # heights = [1, 2, 2]
    # heights = [5, 4, 1, 2]
    # heights = [1, 2, 3, 4, 5]
    # heights = [1, 2, 3, 7, 5, 6]
    # heights = [3, 6, 5, 7, 4, 8, 1, 0]
    print(largestRectangleArea(heights))
