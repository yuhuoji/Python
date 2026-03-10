"""
142 环形链表 II
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while True:
            if not (fast and fast.next):
                return None
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return slow

    def detectCycle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
