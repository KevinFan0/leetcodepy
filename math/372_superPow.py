# 372. 超级次方

"""
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1:

输入: a = 2, b = [3]
输出: 8
示例 2:

输入: a = 2, b = [1,0]
输出: 1024

"""
import json

class Solution:
    # 对base取模运算
    base = 1337

    def superPow(self, a: int, b: list) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self.mypow(a, last)
        part2 = self.mypow(self.superPow(a, b), 10)
        return (part1 * part2) % self.base

    # 计算a的k次方然后与base求模的结果
    def mypow(self, a, k):
        # 对因子求模
        a %= self.base
        res = 1
        for _ in range(k):
            # 这里有乘法，是潜在的溢出点
            res *= a
            # 对乘法结果取模
            res %= self.base
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
            a = int(line);
            line = next(lines)
            b = stringToIntegerList(line);

            ret = Solution().superPow(a, b)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()