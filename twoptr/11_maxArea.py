# 11. 盛最多水的容器

"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""
import json

class Solution:
    def maxArea(self, height: list) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            res = max(res, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
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
            height = stringToIntegerList(line);
            
            ret = Solution().maxArea(height)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()