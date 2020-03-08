# coding:utf-8

import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = i
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[-1]


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
            n = int(line);

            ret = Solution().numSquares(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()