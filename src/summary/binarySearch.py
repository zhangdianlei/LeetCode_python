# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/4 3:20 PM
"""


def binarySearch(A, target):

    start = 0
    end = len(A) - 1

    # 循环判断，直到找到target或者是start > end
    while start <= end:
        mid = (start + end) / 2

        # 返回结果
        if A[mid] == target:
            return mid
        # 舍弃掉左半部分
        if A[mid] < target:
            start = mid + 1
        # 舍弃掉右半部分
        else:
            end = mid - 1

    return end


if __name__ == '__main__':
    print()
