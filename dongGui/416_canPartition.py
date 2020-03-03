# 416. 分割等和子集
# 背包问题或者零钱问题

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

"""


import json

class Solution:
    def canPartition(self, nums: list) -> bool:
        n = len(nums)
        if n == 0:
            return False
        if sum(nums) % 2:
            return False
        amt = int(sum(nums) / 2)
        dp = [[False for _ in range(amt + 1)] for _ in range(n)]
        dp[0][0] = True
        for i in range(1, amt+1):
            if nums[0] == i:
                dp[0][i] = True
                break
        for i in range(1, n):
            for j in range(amt+1):
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
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

            ret = Solution().canPartition(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()