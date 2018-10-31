# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/30 14:57
@python version: 

"""


def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if len(heights) == 0:
        return 0

    h = max(heights)
    s = min(heights)
    ans = 0

    for i in range(s, h + 1):
        start = end = 0
        flag = False

        for j in range(len(heights)):
            if heights[j] >= i:
                end = j + 1
                flag = True
            else:
                if flag:
                    temp = (end - start) * i
                    if temp > ans:
                        ans = temp
                    start = j + 1
                    flag = False
                else:
                    start = j + 1
                    flag = False

            if j == len(heights)-1 and flag:
                temp = (end - start) * i
                if temp > ans:
                    ans = temp

    return ans


if __name__ == '__main__':
    # heights = [2, 1, 5, 6, 2, 3]
    # heights = [2, 2, 1, 1, 1]
    # heights = [2, 4]
    heights = [2, 0, 2]
    print(largestRectangleArea(heights))
