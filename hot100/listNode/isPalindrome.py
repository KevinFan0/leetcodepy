# Definition for singly-linked list.

# 请判断一个链表是否为回文链表。
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 利用python的列表功能 空间复杂度O(n)
        res, h = [], head
        while h:
            res.append(h.val)
            h = h.next
        return res == res[::-1]


    def isPalindrome2(self, head: ListNode) -> bool:
        # 快慢双指针法
        if head is None:
            return True
        # 1. 找到前半部分链表的尾节点
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        first_half_end = slow
        # 2. 反转后半部分的链表
        second_half_start = self.reverse_list(first_half_end)
        # 3. 比较两个部分的值，判断是否为回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        # 4. 恢复链表
        first_half_end.next = self.reverse_list(second_half_start)
        return result


    def reverse_list(self, head):
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


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

            ret = Solution().isPalindrome(head)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()