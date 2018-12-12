# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/27 16:05
@python version: 

"""
import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ListNode(0)
        second = ListNode(0)
        result = ListNode(0)
        start = result

        first.next = l1
        second.next = l2

        if first.next is None and second.next is None:
            return []

        while first.next is not None or second.next is not None:
            if first.next is None:
                result.val = second.next.val
                if second.next.next is not None:
                    result.next = ListNode(0)
                else:
                    break
                result = result.next
                second = second.next
                continue
            if second.next is None:
                result.val = first.next.val
                if first.next.next is not None:
                    result.next = ListNode(0)
                else:
                    break
                result = result.next
                first = first.next
                continue

            if first.next.val < second.next.val:
                result.val = first.next.val
                result.next = ListNode(0)
                result = result.next
                first = first.next
            else:
                result.val = second.next.val
                result.next = ListNode(0)
                result = result.next
                second = second.next

        return start


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()