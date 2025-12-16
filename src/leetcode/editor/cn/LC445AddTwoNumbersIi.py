"""
445 两数相加 II
"""
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-16 头插法等

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 栈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        p1, p2 = l1, l2
        while p1:
            s1.append(p1.val)
            p1 = p1.next
        while p2:
            s2.append(p2.val)
            p2 = p2.next
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode()
        while s1 or s2 or carry:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            # 头插法
            new_node = ListNode(cur % 10)
            new_node.next = dummy.next
            dummy.next = new_node
        return dummy.next
    # leetcode submit region end(Prohibit modification and deletion)


# 反转链表解法
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        dummy = ListNode()
        dummy.next = self.addTwoNumbers206(l1, l2)
        dummy.next = self.reverseList(dummy.next)
        return dummy.next

    # 用l1保存结果
    def addTwoNumbers206(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        s = carry + l1.val + (l2.val if l2 else 0)
        l1.val = s % 10
        l1.next = self.addTwoNumbers206(l1.next, l2.next if l2 else None, carry // 10)
        return l1

    # 反转链表lc206
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


if __name__ == '__main__':
    solution = Solution()

    pass
