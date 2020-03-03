
# coding:utf-8

def solve(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
    res = 0
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
    return res


while True:
    line = input().split(" ")
    print(solve(line[0], line[1]))