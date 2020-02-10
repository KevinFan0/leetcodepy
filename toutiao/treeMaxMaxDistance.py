# 求二叉树中距离最大的两个节点
"""
给定一个二叉树，求出该二叉树中任意两个节点的最远距离（两个节点的距离是指两个节点之间边的条数，可能不过根节点。）

如下图所示的二叉树的最远距离是3

          1
         / \
        2   3
       / \
      4   5
解题思路：虽然最大距离的路径可能不过当前根节点，但是总会过一个子树的根节点的。所以我们可以这么做：
前序遍历二叉树，已当前节点为根节点，分别求出其左右子树的最大深度，相加之后存在一个数组中
接着继续遍历左右子树，分别执行上述操作。遍历完成之后，返回数组中最大的值即可。

"""

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.value = x
        self.left = left
        self.right = right

class Solutiont:
    def __init__(self):
        self.target = []

    def maxDistance(self, root):
        if not root:
            return 0
        self.target.append(self.maxDepth(root.left) + self.maxDepth(root.right))
        self.maxDistance(root.left)
        self.maxDistance(root.right)
        return max(self.target)


    def maxDepth(self, root):
        if not root:
            return 0
        maxleft = self.maxDepth(root.left)
        maxright = self.maxDepth(root.right)
        return max(maxleft, maxright) + 1
