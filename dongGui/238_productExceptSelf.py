# 238. 除自身以外数组的乘积
"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间
"""
import json
class Solution:
    def productExceptSelf(self, nums: list) -> list:
        n = len(nums)
        if n == 0:
            return []
        dpLp = [0 for _ in range(n)]
        dpRp = [0 for _ in range(n)]
        res = []
        dpLp[0], dpRp[-1] = 1, 1
        for i in range(1, n):
            dpLp[i] = dpLp[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            dpRp[i] = dpRp[i + 1] * nums[i + 1]
        for i in range(n):
            res.append(dpLp[i] * dpRp[i])
        return res



def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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

            ret = Solution().productExceptSelf(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()