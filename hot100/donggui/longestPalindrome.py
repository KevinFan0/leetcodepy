# 5. 最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 初始化一个二维表格记录状态
        dp = [[False for _ in range(size)] for _ in range(size)]

        maxLen, start = 1, 0
        for i in range(size):
            # 初始化 单个字符一定是回文
            dp[i][i] = True
        for j in range(1, size):
            # i和j的关系是i <= j ，因此，只需要填这张表的上半部分
            for i in range(0, j):
                if s[i] == s[j]:
                    # 表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # 状态转移方程  dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                # 只要一得到 dp[i][j] = true，就记录子串的长度和起始位置，没有必要截取，因为截取字符串也要消耗性能，记录此时的回文子串的“起始位置”和“回文长度”即可。
                if dp[i][j]:
                    curLen = j - i + 1
                    if curLen > maxLen:
                        maxLen = curLen
                        start = i
        return s[start: start + maxLen]


    def longestPalindrome2(self, s: str) -> str:
        # 暴力匹配
        # 时间复杂度O(N3), 空间复杂度O(1)
        size = len(s)
        if size < 2:
            return s
        max_len, res = 1, s[0]
        # 枚举所有长度大于等于2的子串
        for i in range(size-1):
            for j in range(i+1, size):
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j+1]
        return res

    def __valid(self, s, left, right):
        # 验证子串 s[left, right] 是否为回文串
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right += 1
        return True


def stringToString(input):
    return input[1:-1]


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
            s = stringToString(line);

            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()