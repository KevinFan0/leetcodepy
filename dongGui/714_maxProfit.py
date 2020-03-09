# 714. 买卖股票的最佳时机含手续费

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""
import json

class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        n = len(prices)
        dp = [[0 for i in range(2)] for i in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = float("-inf")
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        return dp[-1][0]

    def maxProfit2(self, prices: list, fee: int) -> int:
        # 直接进行状态转移
        dp_i0, dp_i1 = 0, float("-inf")
        for i in range(len(prices)):
            dp_i0 = max(dp_i0, dp_i1 + prices[i])
            dp_i1 = max(dp_i1, dp_i0 - prices[i] - fee)
        return dp_i0



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
            prices = stringToIntegerList(line);
            line = next(lines)
            fee = int(line);

            ret = Solution().maxProfit2(prices, fee)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()