# 最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]

        maxLen, start = 1, 0
        for i in range(size):
            dp[i][i] = True
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
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