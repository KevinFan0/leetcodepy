# 旋转矩阵
# 顺时针旋转矩阵90度

"""
对于矩阵旋转，最容易想到的便是利用一个大小同样为N*N的临时矩阵T，将原矩阵A[i][j] 放在 T[j][n-i-1]位置处。最后将矩阵T的数据拷贝置矩阵A中，完成矩阵的旋转。但是这种方法的空间复杂度为O(N^2)，不满足题目的O(1)的要求。

其实仔细思考一下，我们可以知道矩阵A中位置[i,j]处的数据，旋转后应该处于[j, n-i-1].按照这个规律，我们可以写出：

[i, j] -> [j, n-i-1] -> [n-i-1, n-j-1] -> [n-j-1, i] -> [i, j]， 即元素旋转后的最终位置构成这样一个循环，因此我们只需要一个循环交换位置，则可以将四个位置的元素放置旋转后的最终位置。
"""

class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)
        for i in range(n):
            for j in range(i, n-i-1):
                t = matrix[i][j]
                cur_i, cur_j = i, j
                next_i, next_j = n - j - 1, i
                while not (next_i == i and next_j == j):
                    matrix[cur_i][cur_j] = matrix[next_i][next_j]
                    cur_i, cur_j = next_i, next_j
                    next_i, next_j = n-cur_j-1, cur_i
                matrix[cur_i][cur_j] = t


















