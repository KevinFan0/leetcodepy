# coding:utf-8
# Definition for a binary tree node.
# 对称二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    """
    镜像二叉树
    要领：将根结点左节点的左节点与根节点的右节点的右节点进行比较
    """
    def isSymmetric2(self, root: TreeNode) -> bool:
        return self.checkMirro(root, root)

    def checkMirro(self, node1, node2):
        if (node1 is None) and (node2 is None):
            return True
        elif node1 is None and node2:
            return False
        elif node2 is None and node1:
            return False
        elif node1.val != node2.val:
            return False
        return self.checkMirro(node1.left, node2.right) and self.checkMirro(node1.right, node2.left)

    # 方法二 迭代
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)
        while queue:
            t1 = queue.pop()
            t2 = queue.pop()
            if (t1 is None) and (t2 is None):
                continue
            if (t1 is None) or (t2 is None):
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

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

            ret = Solution().isSymmetric(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()