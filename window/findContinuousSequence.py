# coding:utf-8
"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""


class Solution:
    def findContinuousSequence(self, target: int) -> list:
        left, right, sum = 1, 1, 0
        res = []
        while right <= ((target + 1) / 2):
            sum += right
            while sum > target:
                sum -= left
                left += 1
            if sum == target:
                tmp = [i for i in range(left, right+1)]
                res.append(tmp)
            right += 1
        return res


s1 = Solution()
print(s1.findContinuousSequence(9))