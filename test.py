# coding:utf-8
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



if __name__ == '__main__':
    # print(solve("aaaccd"))
    t1 = datetime.now()
    time.sleep(2)
    print(type((datetime.now() - t1).microseconds))