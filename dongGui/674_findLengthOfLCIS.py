# 674. 最长连续递增序列
"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
"""

import json
class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0
        curLen, curMax, curLenlist = 1, nums[0], [1]
        for i in range(1, n):
            if curMax < nums[i]:
                curLen += 1
            else:
                curLen = 1
            curMax = nums[i]
            curLenlist.append(curLen)
        return max(curLenlist)


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

            ret = Solution().findLengthOfLCIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()