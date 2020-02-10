# coding:utf-8

# 柱子接雨水问题
"""
给定n个非负整数表示每个宽度为1 的柱子的高度，计算按此排列的柱子下雨之后能接多少雨水

[1,0,1] => 1
[1,2,3] => 0
[2,0,1] => 1
[2,0,2] => 2
[5,4,3,2,3,2,4,5] => 9
"""

# 解题思路: 1. 首先找到数组中最小的那个数
#          2. 存水量取决于最小数左边和右边最大数的最小值

import json
from functools import wraps
from datetime import datetime


def func_cost(fn):
    @wraps(fn)
    def print_cost(*args, **kwargs):
        st = datetime.now()
        fn(*args, **kwargs)
        et = datetime.now()
        print(et - st)
        return
    return print_cost

class Solution:
    # 方法一 直接暴力法
    """
    直接按问题描述进行。对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。
    时间复杂度为O(n2)
    """
    def trap(self, height: list) -> int:
        ans = 0
        for i in range(1, len(height)-1):
            maxleft, maxright = 0, 0
            for j in range(i, -1, -1):
                maxleft = max(maxleft, height[j])
            for j in range(i, len(height)):
                maxright = max(maxright, height[j])
            ans += min(maxleft, maxright) - height[i]
        return ans


    # 方法二 动态编程
    """
    1. 找到数组中从下标 i 到最左端最高的条形块高度 left_max。
    2. 找到数组中从下标 i 到最右端最高的条形块高度 right_max。
    3. 扫描数组 height 并更新答案：
        累加 min(max_left[i], max_right[i])-height[i]到ans上
        
    时间复杂度O(n)
        存储最大高度数组，需要两次遍历，每次O(n)
        最终使用存储度数据更新ans，O(n)
    空间复杂度O(n)额外空间
    """
    # @func_cost
    def trap2(self, height: list) -> int:
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max, right_max = [0] * size, [0] * size
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, size-1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


    # 方法3 利用栈
    """
    1. 使用栈来存储条形块的索引下标。
    2. 遍历数组：
        当栈非空且 height[current]>height[st.top()]
            意味着栈中元素可以被弹出。弹出栈顶元素 top。
            计算当前元素和栈顶元素的距离，准备进行填充操作
                distance=current−st.top()−1
            找出界定高度
                bounded_height=min(height[current],height[st.top()])−height[top]
            往答案中累加积水量 ans+=distance×bounded_height
        将当前索引下标入栈
        将 current 移动到下个位置
    """

    def trap3(self, height: list) -> int:
        ans, current = 0, 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            current += 1
            stack.append(current)
        return ans

    # 双指针法
    """
    1. 初始化left指针为0并且right指针为size-1
    2. while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                更新left_max
            else:
                累加left_max - height[left]到ans
            left = left + 1
        else:
            if height[right] >= right_max:
                更新right_max
            else:
                更新right_max - height[right]到ans
            right = right - 1
    """
    def trap4(self, height: list) -> int:
        if len(height) == 0:
            return 0
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[right]
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left = left + 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right = right - 1
        return ans





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

            ret = Solution().trap4(height)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
