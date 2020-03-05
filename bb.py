
# coding:utf-8

def solve(s1):
    s1 = s1.lower()
    s1.replace(" ", "0")
    return s1[::-1]



while True:
    str = input()
    s1 = str.lower()
    s1 = s1.replace(" ", "0")
    print(s1[::-1])