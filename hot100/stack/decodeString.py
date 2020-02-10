# coding:utf-8
# 394 字符串解码

# "3[a]2[bc]"

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, nums = [], "", 0
        if len(s) == 0:
            return ""
        for i in range(len(s)):
            if s[i].isdigit():
                nums = nums * 10 + int(s[i])
            elif s[i] == "[":
                stack.append([nums, res])
                res, nums = "", 0
            elif s[i] == "]":
                cur_num, last_res = stack.pop()
                res = last_res + cur_num * res
            else:
                res += s[i]
        return res


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

            ret = Solution().decodeString(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()