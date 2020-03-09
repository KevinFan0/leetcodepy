# 221. 最大正方形
"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

"""
class Solution:
    def maximalSquare(self, matrix: list) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxlen = 0
        dp = [[0 for _ in range(n)] for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if matrix:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    maxlen = max(dp[i][j], maxlen)
        return maxlen * maxlen
