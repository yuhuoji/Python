"""
460 LFU 缓存
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-01-16
# 标准库
# 手写双向链表
# leetcode submit region begin(Prohibit modification and deletion)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    lfu.get(1)
    lfu.put(3, 3)
    lfu.get(2)
    lfu.get(3)
    pass
