# coding:utf-8
# 63 不同路径2

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        dp = [[0] * len(item) for item in obstacleGrid]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i == j == 0:
                    if obstacleGrid[i][j]:
                        return 0
                    else:
                        dp[i][j] = 1
                elif obstacleGrid[i][j]:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles(grid))