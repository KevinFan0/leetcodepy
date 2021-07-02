import json

class Solution:
    memo = {}

    def findTargetSumWays2(self, nums, target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.helper(nums, 0, target)

    def helper(self, nums, i, rest):
        if i == len(nums):
            if rest == 0:
                return 1
            else:
                return 0
        key = (i, rest)
        if key in self.memo.keys():
            return self.memo.get(key)
        res = self.helper(nums, i + 1, rest - nums[i]) + self.helper(nums, i + 1, rest + nums[i])
        self.memo[key] = res
        return res

    def findTargetSumWays(self, nums, target: int) -> int:
        numSum = sum(nums)
        if numSum < target or ((target + numSum) % 2 == 1):
            return 0
        return self.helper2(nums, (target + numSum) // 2)



    def helper2(self, nums, sum):
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-num[i-1]]
        dp = [[0 for _ in range(sum + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(0, sum + 1):
                # 判断背包空间是否充足
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    # 背包的空间不足，只能选择不装物品
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][sum]



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
            line = next(lines)
            target = int(line);

            ret = Solution().findTargetSumWays(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()