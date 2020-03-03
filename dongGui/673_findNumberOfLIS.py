# 673. 最长递增子序列的个数

"""
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""

import json

class Solution:
    def findNumberOfLIS(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for _ in range(n)]
        dp_count = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j] + 1
                        dp_count[i] = dp_count[j]
                    elif dp[j] + 1 == dp[i]:
                        dp_count[i] += dp_count[j]
        res = 0
        maxlen = max(dp)
        for i in range(n):
            if dp[i] == maxlen:
                res += dp_count[i]
        return res


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

            ret = Solution().findNumberOfLIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()