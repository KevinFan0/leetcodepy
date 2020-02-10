# Definition for singly-linked list.
# 给定一个链表，判断链表中是否有环。

import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 哈希方法
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        tmp = set()
        while head:
            if head in tmp:
                return True
            tmp.add(head)
            head = head.next
        return False

    # 快慢指针法
    def hasCycle2(self, head: ListNode) -> bool:
        if head is None and (head.next is None):
            return False
        i, j = head, head.next
        while j and j.next:
            if i == j:
                return True
            # i每次走一步，j每次走两步
            i = i.next
            j = j.next.next
        return False



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

            ret = Solution().hasCycle(head, pos)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()