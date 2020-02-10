# coding:utf-8
# 53 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

import json

class Solution:
    def maxSubArray(self, nums: list) -> int:
        # 利用贪心算法
        if len(nums) == 0:
            return 0
        cur_sum, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])
            res = max(res, cur_sum)
        return res


    # 动态规划
    def maxSubArray2(self, nums: list) -> int:
        res, sum = nums[0], 0
        for i in range(len(nums)):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(res, sum)
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

            ret = Solution().maxSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()