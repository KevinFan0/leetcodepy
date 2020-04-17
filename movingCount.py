#  机器人的运动范围

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # BFS
        queue, visited = [(0, 0)], set()
        while queue:
            i, j = queue.pop(0)
            if i >= m or j >= n or (i, j) in visited or self.digitsum(i) + self.digitsum(j) > k:
                continue    
            visited.add((i, j))
            queue.append((i+1, j))
            queue.append((i, j + 1))
        return len(visited)

    def digitsum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

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
            m = int(line);
            line = next(lines)
            n = int(line);
            line = next(lines)
            k = int(line);

            ret = Solution().movingCount(m, n, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()