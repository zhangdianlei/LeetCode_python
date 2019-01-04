# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com
@time: 2019/1/4 3:20 PM
"""


def binarySearch(A, target):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
            return mid
        if A[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == '__main__':
    print()
