# 322. 零钱兑换
"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
"""
import json

class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        # 一维dp解法
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1



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
            coins = stringToIntegerList(line);
            line = next(lines)
            amount = int(line);

            ret = Solution().coinChange2(coins, amount)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()