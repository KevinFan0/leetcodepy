# 152  乘积最大子序列

"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""

import json

class Solution:
    def maxProduct(self, nums: list) -> int:
        """
        维护两个数组 dp_max和dp_min

        """
        n = len(nums)
        if n == 0:
            return 0
        dp_max = [0 for _ in range(n + 1)]
        dp_min = [0 for _ in range(n + 1)]
        maxres = float("-inf")
        dp_max[0], dp_min[0] = 1, 1
        for i in range(1, n + 1):
            if nums[i-1] < 0:
                dp_max[i-1], dp_min[i-1] = dp_min[i-1], dp_max[i-1]
            dp_max[i] = max(dp_max[i-1] * nums[i-1], nums[i-1])
            dp_min[i] = min(dp_min[i-1] * nums[i-1], nums[i-1])
            maxres = max(dp_max[i], maxres)
        return maxres


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

            ret = Solution().maxProduct(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()