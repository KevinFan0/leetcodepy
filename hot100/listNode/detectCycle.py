# Definition for singly-linked list.
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 哈希方法
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        tmp = set()
        while head:
            if head in tmp:
                return head
            tmp.add(head)
            head = head.next
        return None

    # 快慢指针法
    def detectCycle2(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast



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
            line = next(lines)
            pos = int(line);

            ret = Solution().detectCycle(head, pos)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()