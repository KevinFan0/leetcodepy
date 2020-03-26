# 0-1背包问题
"""
给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，最多能装的价值是多少？

举个简单的例子，输入如下：

N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]

输出：6
"""

def solve(weights, values, n, w):
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j - weights[i-1] < 0:
                # 当前背包容量装不下，只能选择不装入背包
                dp[i][j] = dp[i-1][j]
            else:
                # 装入或者不装入背包，择优
                dp[i][j] = max(dp[i-1][j-weights[i-1]] + values[i-1],
                               dp[i-1][j])
    return dp[-1][-1]


if __name__ == '__main__':
    weights = [2, 1, 3]
    values = [4, 2, 3]
    print(solve(weights, values, 3, 4))
