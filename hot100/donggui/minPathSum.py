# 64 最小路径和

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

"""
解题思路:
1. 创建二维数组存储这个网格（本题中就是grid本身）grid(i, j)
2. grid(i,j)表示第i行第j个数字
目的是找grid（0，0）到grid（m-1， n-1）即MinSum((0,0), (m-1,n-1))
状态转移方程为   dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))


        dp问题：利用列表进行存储，每一行每个步骤结束后的最小值，那么在最后一行，其最小值为min（4+dp[0],4+dp[1],1+dp[0],1+dp[1]...）
        所以状态转移方程为： 如果i==0 or i==len(triangle[row]) 那么其转移方程为dp[i]=dp[0]triangle[row][i]  dp[i]=dp[i-1]+triangle[row][i]
"""

class Solution:
    # 二维状态方程解法
    def minPathSum(self, grid: list) -> int:
        # 第一步先创建二维数组保存状态 就是grid本身
        m = len(grid)
        if m <= 1:
            return sum(grid[0])
        dp = [[0] * len(item) for item in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # 边界只有一个邻边
                if j == 0 and i == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0:
                    dp[0][j] = grid[0][j] + dp[0][j-1]
                elif j == 0:
                    dp[i][0] = grid[i][0] + dp[i-1][0]
                else:
                    # 当前取值，在上一层的邻边最小值相加
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][-1]

    # 一维状态方程解法（原地建立状态方程）
    def minPathSum2(self, grid: list) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        print(grid)
        return grid[-1][-1]


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1],
]
if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum2(grid))