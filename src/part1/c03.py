class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(str(s)) == 0:
            return 0
        else:
            s = str(s)
            total_length = len(s)
            length = 1
            start = 0

            while start < total_length:
                tempSet = set()
                tempSet.add(s[start])

                for end in range(start+1, total_length):

                    if s[end] not in tempSet:
                        tempSet.add(s[end])
                    else:
                        if len(tempSet) > length:
                            length = len(tempSet)
                        break

                    if end == total_length-1:
                        if len(tempSet) > length:
                            length = len(tempSet)
                        return length
                start = start + 1

        return length


def stringToString(input):
    import json

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
            s = stringToString(line);

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()