# coding:utf-8
# 70 爬楼梯
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归法
        # 将问题拆分成一次爬一个和一次爬两个
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    # 动态规划
    def climbStairs2(self, n: int) -> int:
        # 用一个数组将已经计算的结果记录
        tmp = [0] * (n+1)
        if n == 1:
            return 1
        tmp[0] = 1
        tmp[1] = 2
        for i in range(2, n+1):
            tmp[i] = tmp[i-1] + tmp[i-2]
        return tmp[n-1]

    # 斐波那契数列法
    def climbStairs3(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n+1):
            first, second = second, first + second
        return second



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
            n = int(line);

            ret = Solution().climbStairs3(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()