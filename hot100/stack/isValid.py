# 20 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        if len(s) == 0:
            return True
        for i in s:
            if i in maps.keys():
                stack.append(i)
            else:
                if stack:
                    if i == maps[stack[-1]]:
                        stack.pop()
                        continue
                return False
        return False if stack else True

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

            ret = Solution().isValid(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()