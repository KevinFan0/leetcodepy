#3.无重复字符的最长子串
# 时间窗问题

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        curlen, maxlen, left = 0, 0, 0
        lookup = set()
        for i in range(len(s)):
            curlen += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curlen -= 1
            if curlen > maxlen:
                maxlen = curlen
            lookup.add(s[i])
        return maxlen

def stringToString(input):
    return input[1:-1]

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