# 约瑟夫环问题
"""
已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围，从编号为k的人开始报数，数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，直到圆桌周围的人只有一个没有出列。假设n=1000,k=5,m=13,问剩下最后一个人编号。
"""

def joseph_problem(n, k, m):
    joseph_arr = []
    for i in range(1, n+1):
        joseph_arr.append(i)
    start = k
    length = len(joseph_arr)

    for j in range(length-1):
        start = (start + m) % len(joseph_arr)
        joseph_arr.pop(start)

    return joseph_arr[0]


if __name__ == '__main__':
    last_num = joseph_problem(41, 1, 3)
    print(last_num)