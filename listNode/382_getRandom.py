# 382. 链表随机节点
"""
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

示例:

// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();
"""


# Definition for singly-linked list.
import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    # 返回链表中的一个随机节点的值
    def getRandom(self):
        i, res = 0, 0
        p = self.head
        while p:
            # 生成一个 [0, i) 之间的整数
            # 这个整数等于 0 的概率就是 1/i
            i += 1
            if random.randint(0, i-1) == 0:
                res = p.val
            p = p.next
        return res
# Your Solution object will be instantiated and called as such:
head = ListNode(1)
obj = Solution(head)
param_1 = obj.getRandom()
print(param_1)