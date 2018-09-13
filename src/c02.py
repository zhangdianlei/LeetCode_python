# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/9/12 10:42
@python version: 

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        # root = ListNode()

        tempSum = l1.val + l2.val
        quotient = tempSum//10
        remainder = tempSum % 10
        result.append(remainder)

        # nextNode = ListNode()
        # root.val = remainder
        # root.next = nextNode

        while l1.next is not None or l2.next is not None:

            if l1.next is not None:
                l1 = l1.next
            else:
                l1 = ListNode(0)

            if l2.next is not None:
                l2 = l2.next
            else:
                l2 = ListNode(0)

            tempSum = l1.val + l2.val + quotient
            quotient = tempSum // 10
            remainder = tempSum % 10
            result.append(remainder)
            #
            # nextNode.val = remainder
            # nextNode.next = ListNode()

        if remainder == 1:
            result.append(remainder)
        #
        # res_list = ListNode()
        #
        # for index, item in result:
        #     res_list.val = item
        #     res_list = res_list.next
        #
        print('result', result)
        # print(listNodeToString(l1))
        return


def stringToIntegerList(input):
    return map(int, str(input))


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
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
