# 875. 爱吃香蕉的珂珂
# 二分查找

"""
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
 

提示：

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9


"""
import json

class Solution:
    def minEatingSpeed(self, piles: list, H: int) -> int:
        if len(piles) == 0:
            return 0
        # 套用搜索左侧边界的算法框架
        left, right = 1, max(piles)
        while left < right:
            mid = int(left + (right - left) / 2)
            if self.canfinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left

    def canfinish(self, piles, speed, H):
        time = 0
        for item in piles:
            time += self.timeOf(item, speed)
        return time <= H

    def timeOf(self, n, speed):
        return n // speed + 1 if n % speed else n // speed


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
            piles = stringToIntegerList(line);
            line = next(lines)
            H = int(line);

            ret = Solution().minEatingSpeed(piles, H)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()