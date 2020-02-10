# coding:utf-8

# 23. 合并K个排序链表
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""

from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        # 循环迭代， 两两合并排序（虽然能解决问题，但复杂度太高）
        if len(lists) == 0:
            return None
        res = lists[0]
        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])

        return res

    # 暴力法，将所有节点放到一个list然后进行排序
    def mergeKLists2(self, lists: list) -> ListNode:
        tmp = []
        head = point = ListNode(0)
        for i in range(len(lists)):
            p = lists[i]
            while p:
                tmp.append(p.val)
                p = p.next
        # 对这个list进行排序
        for item in sorted(tmp):
            point.next = ListNode(item)
            point = point.next
        return head.next

    # 逐一比较，优先队列优化
    def mergeKLists3(self, lists: list) -> ListNode:
        """
        1 比较k个节点（每个链表的首节点），获得最小值的节点
        2 将选中的节点接在最终有序链表的后面

        时间复杂度 O(Nlogk)
        空间复杂度 O(n)
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

    # 分治
    def mergeKLists4(self, lists: list) -> ListNode:
        count = len(lists)
        interval = 1
        while interval < count:
            for i in range(0, count - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if count > 0 else lists


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
