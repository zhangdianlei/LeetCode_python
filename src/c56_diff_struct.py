# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/18 16:30
@python version: 

"""


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals.sort()
    result = []
    while len(intervals) > 1:

        a = intervals.pop(0)
        b = intervals.pop(0)
        if a[1] >= b[0]:
            c = [a[0], b[1]]
            intervals.insert(0, c)
        else:
            result.append(a)
            intervals.insert(0, b)

    if len(intervals) == 1:
        result.append(intervals[0])

    return result


if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [5, 6]]
    # intervals = [[1, 4], [4, 5]]
    # intervals = [[1, 4]]
    intervals = []

    print(merge(intervals))
