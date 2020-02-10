# Definition for singly-linked list.
# 编写一个程序，找到两个单链表相交的起始节点。
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 哈希表方法
        tmp = set()
        while headA:
            tmp.add(headA)
            headA = headA.next
        while headB:
            if headB in tmp:
                return headB
            headB = headB.next
        return None

    # 双指针
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptra, ptrb = headA, headB
        while ptra != ptrb:
            ptra = ptra.next if ptra else headB
            ptrb = ptrb.next if ptrb else headA
        return ptra



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
            intersectVal = int(line);
            line = next(lines)
            listA = stringToListNode(line);
            line = next(lines)
            listB = stringToListNode(line);
            line = next(lines)
            skipA = int(line);
            line = next(lines)
            skipB = int(line);

            ret = Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()