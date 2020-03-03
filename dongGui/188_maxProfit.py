# 188  买卖股票的最佳时机 IV

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

"""
import json
class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        #  python超时
        n = len(prices)
        if n == 0:
            return 0
        # 贪心算法
        if k > len(prices):
            profit = 0
            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                profit += (diff if diff > 0 else 0)
            return profit
        dp = [[[0 for i in range(2)] for i in range(k + 1)] for i in range(n)]
        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]

    def maxProfit2(self, k: int, prices: list) -> int:
        # 贪心算法 + 动态规划
        if not prices:
            return 0
        # 贪心算法
        if k > len(prices):
            profit = 0
            for i in range(1, len(prices)):
                diff = prices[i] - prices[i - 1]
                profit += (diff if diff > 0 else 0)
            return profit
        # 动态规划
        dpI0 = [0] * (k + 1)
        dpI1 = [-float('INF')] + [-prices[0]] * k
        print(dpI1)
        for i in range(1, len(prices)):
            for k in range(1, k + 1):
                dpI0[k] = max(dpI0[k], dpI1[k] + prices[i])
                dpI1[k] = max(dpI1[k], dpI0[k - 1] - prices[i])
        return dpI0[k]


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
            k = int(line);
            line = next(lines)
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(k, prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()