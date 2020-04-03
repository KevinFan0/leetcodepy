# 130. 被围绕的区域
"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""

"""
二维坐标(x,y)可以转换成x * n + y这个数（m是棋盘的行数，n是棋盘的列数）。敲黑板，这是将二维坐标映射到一维的常用技巧。
"""

from Union_Find import UF

class Solution:
    def solve(self, board:list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not len(board):
            return
        m, n = len(board), len(board[0])
        root = m * n
        uf = UF(m * n + 1)      # 给root留一个位置
        # 将首列和末列的O与root连通
        for i in range(m):
            if board[i][0] == "O":
                uf.union(i * n, root)
            if board[i][n - 1] == "O":
                uf.union(i * n + n - 1, root)
        # 将首行和末行的O与root连通
        for i in range(n):
            if board[0][i] == "O":
                uf.union(i, root)
            if board[m-1][i] == "O":
                uf.union(n * (m-1) + i, root)
        # 方向数组 d 是上下左右搜索的常用手法
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O":
                    #将此 O 与上下左右的 O 连通
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == "O":
                            uf.union(x * n + y, i * n + j)

        # 所有不和 dummy 连通的 O，都要被替换
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not uf.connected(root, i * n +j):
                    board[i][j] = "X"
        print(uf.parent)

if __name__ == '__main__':
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    s = Solution()
    s.solve(board)
    print(board)






















