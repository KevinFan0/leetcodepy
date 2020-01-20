# 最小覆盖子串


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass

def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            line = next(lines)
            t = stringToString(line);

            ret = Solution().minWindow(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()