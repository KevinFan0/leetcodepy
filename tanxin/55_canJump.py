# 55. 跳跃游戏
"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""
import json

class Solution:
    def canJump(self, nums:list) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n-1):
            # 不断计算能跳到最远的距离
            farthest = max(farthest, nums[i] + i)
            # 可能碰到0 卡住跳不动了
            if farthest <= i:
                return False
        return farthest >= n-1


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

            ret = Solution().canJump(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()