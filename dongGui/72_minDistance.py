# 72. 编辑距离

"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 递归解法
        # 递归+备忘录
        memo = dict()       # 备忘录
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min(dp(i-1, j) + 1,  # 删除
                           dp(i, j-1) + 1,  # 插入
                           dp(i-1, j-1) + 1,#替换
                )
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        # 动态规划法
        # dp[i-1][j-1]表示存储words1[0.....i]和words2[0.....i]的最小编辑距离
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # base case
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        # 自底向上求解
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j-1] + 1
                    )
        return dp[-1][-1]


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
            word1 = stringToString(line);
            line = next(lines)
            word2 = stringToString(line);

            ret = Solution().minDistance(word1, word2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()