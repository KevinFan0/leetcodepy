# 494. 目标和
"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
"""
import json

class Solution:

    def findTargetSumWays(self, nums: list, S: int) -> int:
        # 方法一 递归法 + 备忘录
        memo = {}
        res = self.helper(0, 0, nums, S, 0, memo)
        return res

    def helper(self, index, sum, nums, target, res, memo):
        if (index, sum) in memo.keys():
            return memo[(index, sum)]
        if index == len(nums):
            if sum == target:
                res += 1
        else:
            res = self.helper(index+1, sum+nums[index], nums, target, res, memo) + self.helper(index+1, sum-nums[index], nums, target, res, memo)
        memo[(index, sum)] = res
        return res


    # 动态规划
    def findTargetSumWays2(self, nums: list, S: int) -> int:
        dp = [[0 for _ in range(S)] for _ in range(len(nums)+1)]
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            for j in range(S):
                dp[i][j] = dp[i-1][j+nums[i]] + dp[i-1][j-nums[i]]
        return dp[-1][-1]



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
            nums = stringToIntegerList(line);
            line = next(lines)
            S = int(line);

            ret = Solution().findTargetSumWays(nums, S)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()