# 整数反转
import pdb


class Solution:
    # 将数字转成字符串数组然后反转（注意边界值和符号）
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
        res = int(str([int(x) for x in map(int, str(x))][::-1]).replace(", ", "").replace("[", "").replace("]", "")) * sign
        if (-2) ** 31 <= res <= 2 ** 31 - 1:
            return res
        return 0

    # 数学方法
    def reverse2(self, x: int) -> int:
        rev = 0
        temp1 = abs(x)
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while temp1 != 0:
            pop = temp1 % 10
            temp1 = temp1 // 10
            rev = rev * 10 + pop
            if rev > of:
                return 0
        return rev if x > 0 else -rev




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
            x = int(line)

            ret = Solution().reverse2(x)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()