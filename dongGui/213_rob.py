# 213. 打家劫舍2

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1,3,4]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

"""

"""
n=1     num[0]                                      dp[0]
n=2     max(num[0], num[1])                         dp[1] = max(dp[0], num[n-1])                
n=3     num[1]                                      dp[2] = max(dp[1], num[n-1])
n=4     max(num[0] + num[2], num[1] + num[3])       dp[3] = max(dp[2]
n=5     max(dp[4], num[2]+num[4])
n=6     max(dp[5], num[1] + num[3] + num[5])
"""
import json
class Solution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp1 = [0 for i in range(n+1)]
        # 先计算不考虑第一间房子所能偷的最多
        # 再计算不考虑最后一间房子所能偷的最多，
        dp1[0], dp1[1] = 0, 0
        for i in range(2, n+1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i-1])
        dp2 = [0 for i in range(n + 1)]
        dp2[0], dp2[1] = 0, nums[0]
        for i in range(2, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i - 1])
        return max(max(dp1), max(dp2))


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

            ret = Solution().rob(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()