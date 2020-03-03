# 337 打家劫舍III
"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

"""

"""
解题思路：
n=1         root.val
n=2         max(root.val, root.left(right).val)
n=3         max(单个, root.val+root.left.left(right), root.left + root.right)
即 爷爷和孙子一起偷的与父亲这一辈的比较大小
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 递归法
        if not root:
            return 0
        sum = root.val
        if root.left is not None:
            sum += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right is not None:
            sum += self.rob(root.right.left) + self.rob(root.right.right)
        return max(sum, self.rob(root.right) + self.rob(root.left))

    # 方法二
    def rob2(self, root: TreeNode) -> int:
        # 创建字典存储状态
        res = {}
        return self.helper(root, res)

    def helper(self, root, res):
        if not root:
            return 0
        if root in res.keys():
            return res.get(root)
        sum = root.val
        if root.left is not None:
            sum += self.helper(root.left.left, res) + self.helper(root.left.right, res)
        if root.right is not None:
            sum += self.helper(root.right.left, res) + self.helper(root.right.right, res)
        result = max(sum, self.rob(root.right) + self.rob(root.left))
        res[root] = result
        return result


    # 方法三
    def rob3(self, root: TreeNode) -> int:
        """
        root[0] = Math.max(rob(root.left)[0], rob(root.left)[1]) + Math.max(rob(root.right)[0], rob(root.right)[1])
        root[1] = rob(root.left)[0] + rob(root.right)[0] + root.val
        """
        res = self.helper2(root)
        return max(res[0], res[1])

    def helper2(self, root):
        if not root:
            return [0] * 2
        dp = [0] * 2
        left = self.helper2(root.left)
        right = self.helper2(root.right)
        dp[0] = max(left[0], left[1]) + max(right[0], right[1])
        dp[1] = left[0] + right[0] + root.val
        return dp


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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
            root = stringToTreeNode(line);

            ret = Solution().rob(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()