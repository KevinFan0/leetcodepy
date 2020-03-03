"""
手动实现lru算法
"""
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.queue = OrderedDict()

    def get(self, key):
        if key not in self.queue:
            # 要找的数据不在缓存中返回-1
            return -1
        value = self.queue.pop(key)         # 将命中缓存的数据移除
        self.queue[key] = value             # 将命中缓存的数据重新添加到头部
        return self.queue[key]


    def put(self, key, value):
        if key in self.queue:
            # 如果已经在缓存中，则先移除老的数据
            self.queue.pop(key)
        elif len(self.queue.items()) == self.cap:
            self.queue.popitem(last=False)            # 如果不在缓存中并且达到最大容量则把最后的数据淘汰(最先存到queue中到）
        self.queue[key] = value                         # 将新数据添加到头部



# lru算法的哈希表+双链表实现

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None


class LRUCache2():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Pop the current tail."""
        res = self.tail.prev
        self._remove_node(res)
        return res


    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        # move the accessed node to the head;
        self._move_to_head(node)
        return node.val

    def put(self, key, value):
        node = self.cache.get(key, None)
        if not node:
            newNode = DLinkedNode()
            newNode.key, newNode.val = key, value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # 删掉尾部的元素
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.val = value
            self._move_to_head(node)
