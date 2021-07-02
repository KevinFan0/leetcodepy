# coding:utf-8
import json
from datetime import datetime
import time


def solve(s):
    left, right = 0, 1
    res, num = "", 1
    s += "0"
    while right < len(s):
        if s[right] == s[left]:
            num += 1
        else:
            if num == 1:
                res += s[left]
            else:
                res += str(num-1) + s[left]
            num = 1
            left = right
        right += 1
    return res



class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution:
    def solve(self, root):
        if not root:
            return root
        queue, data = [root], []
        while len(queue) > 0:
            node = queue.pop(0)
            data.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data


class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        res = 0
        if root == None:
            return res
        queue = [root]
        while queue:
            cnt = len(queue)
            res += 1
            while cnt > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return res
                cnt -= 1
        return res


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

            ret = Solution2().minDepth(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()