# 647. 回文子串
"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        count += 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        return count


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

            ret = Solution().countSubstrings(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()