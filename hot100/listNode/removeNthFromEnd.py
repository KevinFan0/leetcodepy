# 删除链表的倒数第N个节点
import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 删除倒数第N个节点等价于删除整数第len(head) - n + 1个节点问题
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 方法一 利用双指针
        tmptr = ListNode(0)
        tmptr.next, ptr = head, head
        lenhead = 0
        while ptr:
            lenhead += 1
            ptr = ptr.next
        lenhead -= n
        ptr = tmptr
        while lenhead > 0:
            lenhead -= 1
            ptr = ptr.next
        ptr.next = ptr.next.next
        return tmptr.next


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
            head = stringToListNode(line)
            line = next(lines)
            n = int(line)

            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()