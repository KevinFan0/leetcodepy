# 1248 统计「优美子数组」
"""
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

"""
import json

class Solution:
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        if not list:
            return 0
        res, i = 0, 1
        odd = [-1]    # 记录奇数的下标
        for j in range(0, len(nums) + 1):
            if j == len(nums) or nums[j] % 2:
                odd.append(j)
            if len(odd) - i > k:
                left = odd[i] - odd[i-1]
                right = j - odd[len(odd) - 2]
                res = res + left * right
                i += 1
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
            line = next(lines)
            k = int(line);

            ret = Solution().numberOfSubarrays(nums, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()