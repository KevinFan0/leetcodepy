# 95. 不同的二叉搜索树 II


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> list:
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None, ]
        tmp = []
        for i in range(start, end+1):
            left = self.helper(start, i-1)
            right = self.helper(i+1, end)
            # 最后将左子树和右子树连接到root上
            for l in left:
                for r in right:
                    curroot = TreeNode(i)
                    curroot.left = l
                    curroot.right = r
                    tmp.append(curroot)
        return tmp

