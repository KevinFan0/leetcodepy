# 最小的k个数
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""

import json
import heapq

class Solution:
    def getLeastNumbers(self, arr: list, k: int) -> list:
        return heapq.nsmallest(k, arr)


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
            arr = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution().getLeastNumbers(arr, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()