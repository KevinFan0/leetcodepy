# 82. 删除排序链表中的重复元素 II

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 首先加空指针为链表的头，防止开头就出现重复数字
        newhead = ListNode(0)
        newhead.next = head
        # pre为前驱指针，cur为当前指针
        pre, cur = None, newhead
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                t = cur.val
                while cur and cur.val == t:
                    # 去掉与cur.val相同的节点
                    cur = cur.next
                # 找到与cur.val不相同的节点
                pre.next = cur
        return newhead.next


    # 递归法
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next and head.val == head.next.val:
            # 开始找相同数
            while head and head.next and head.val == head.next.val:
                # 忽略所有相同的数
                head = head.next
            # 从下一个不同的数开始递归
            return self.deleteDuplicates2(head.next)
        else:
            head.next = self.deleteDuplicates2(head.next)
        return head


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


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
            head = stringToListNode(line);

            ret = Solution().deleteDuplicates(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()