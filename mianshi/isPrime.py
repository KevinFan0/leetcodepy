# 高效查找素数


# 返回区间【2，n）中有多少个素数

import math
def countPrime(n):
    isprime = [True for _ in range(n)]
    for i in range(2, math.ceil(math.sqrt(n))):
        if isprime[i]:
            for j in range(i*i, n, i):
                isprime[j] = False
    cnt = 0
    for i in range(2, n):
        if isprime[i]:
            cnt += 1
    return cnt

print(countPrime(100))