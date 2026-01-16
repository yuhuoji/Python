"""
146 LRU 缓存
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-01-16
# 标准库
# 手写双向链表

# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    __slots__ = 'key', 'value', 'prev', 'next'

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.remove(node)
        self.move_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            self.key_to_node[key] = node = Node(key, value)
        else:
            node = self.key_to_node[key]
            node.value = value
            self.remove(node)
        self.move_front(node)
        if len(self.key_to_node) > self.capacity:
            node = self.dummy.prev
            del self.key_to_node[node.key]
            self.remove(node)

    # 将节点x移动到链表头部
    def move_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

    # 删除节点x
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
        x.prev = None
        x.next = None


class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.get(1)
    lRUCache.put(3, 3)
    lRUCache.get(2)
    lRUCache.put(4, 4)
    lRUCache.get(1)
    lRUCache.get(3)
    lRUCache.get(4)
    pass
