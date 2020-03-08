# 96. 不同的二叉搜索树

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

    # 递归+备忘录
    def numTrees2(self, n: int) -> int:
        if (n == 0):
            return 0
        memo = {}
        return self.helper(1, n, memo)


    def helper(self, start, end, memo):
        if (start > end):
            return 1
        sum = 0
        key = (start, end)
        if key in memo.keys():
            return memo[key]
        for i in range(start, end+1):
            sum += self.helper(start, i - 1, memo) * self.helper(i + 1, end, memo)
        memo[(start, end)] = sum
        return sum



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

            ret = Solution().numTrees2(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()