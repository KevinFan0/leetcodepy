# coding:utf-8
# 利用python实现栈


class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None

    def length(self):
        return self._size

    def pop(self):
        assert not self.isEmpty()
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

    # return the top item on the stack without removing it.
    def peek(self):
        assert not self.isEmpty()
        return self._top.item

