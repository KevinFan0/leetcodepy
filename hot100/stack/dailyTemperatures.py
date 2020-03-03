# 739. 每日温度
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
import json

class Solution:
    def dailyTemperatures(self, T: list) -> list:
        # 把温度数组的index存入栈中
        if len(T) == 0:
            return []
        stack, res = [], [0] * len(T)
        for index, value in enumerate(T):
            while stack and value > T[stack[-1]]:
                res[stack.pop()] = index - stack[-1]
            stack.append(index)
        return res


    def dailyTemperatures2(self, T: list) -> list:
        # 单调栈解法
        if len(T) == 0:
            return []
        stack, res = [], [0] * len(T)
        for i in range(len(T)-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
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
            T = stringToIntegerList(line);

            ret = Solution().dailyTemperatures(T)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()