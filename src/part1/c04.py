# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/13 20:50
@python version: 

"""
import json


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = [1, 2]
        nums2 = [3, 4]

        mean = int((len(nums1) + len(nums2) + 1) / 2)
        totalLength = len(nums1) + len(nums2)

        if (totalLength % 2) == 0:

            min = 0
            pointer = 0

            while pointer < mean:
                if len(nums1) > 0 and len(nums2) > 0:
                    if nums1[0] > nums2[0]:
                        min = nums2.pop(0)
                    else:
                        min = nums1.pop(0)

                elif len(nums1) == 0:
                    min = nums2.pop(0)

                elif len(nums2) == 0:
                    min = nums1.pop(0)

                pointer = pointer + 1

            min_nums1 = 0
            min_nums2 = 0

            if len(nums1) == 0:
                min_nums1 = nums2[0]
            else:
                min_nums1 = nums1[0]

            if len(nums2) == 0:
                min_nums2 = nums1[0]
            else:
                min_nums2 = nums2[0]

            if min_nums1 >= min_nums2:
                return (min + min_nums2) / 2
            else:
                return (min + min_nums1) / 2

        else:
            min = 0
            pointer = 0

            while pointer < mean:
                if len(nums1) > 0 and len(nums2) > 0:
                    if nums1[0] > nums2[0]:
                        min = nums2.pop(0)
                    else:
                        min = nums1.pop(0)

                elif len(nums1) == 0:
                    min = nums2.pop(0)

                elif len(nums2) == 0:
                    min = nums1.pop(0)

                pointer = pointer + 1

            return min


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
