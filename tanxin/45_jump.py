# 45. 跳跃游戏 II
"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

"""
import json

class Solution:
    def jump(self, nums: list) -> int:
        # 备忘录+动态规划 超时
        memo = [len(nums)] * len(nums)
        def dp(nums, index):
            n = len(nums)
            if index >= n-1:
                return 0
            if memo[index] != n:
                return memo[index]
            steps = nums[index]
            # 你可以选择跳1步，2步。。。
            for i in range(1, steps + 1):
                # 穷举每一个选择
                # 计算每一个子问题的结果
                subProblem = dp(nums, index + i)
                memo[index] = min(subProblem + 1, memo[index])
            return memo[index]
        return dp(nums, 0)

    def jump2(self, nums:list) -> int:
        # 贪心算法
        n = len(nums)
        end, farthest = 0, 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                jumps += 1
                end = farthest
        return jumps




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

            ret = Solution().jump(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()