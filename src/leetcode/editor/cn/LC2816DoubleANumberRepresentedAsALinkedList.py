"""
2816 翻倍以链表形式表示的数字
"""
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-17 特定解法2

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.val > 4:
            head = ListNode(0, head)
        cur = head
        while cur:
            sum = cur.val * 2 + (1 if cur.next and cur.next.val > 4 else 0)
            cur.val = sum % 10
            cur = cur.next
        return head


# leetcode submit region end(Prohibit modification and deletion)


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        carry = 0
        cur = head
        pre = None
        while cur or carry:
            if not cur:
                pre.next = ListNode(carry)
                break
            carry += cur.val * 2
            cur.val = carry % 10
            carry //= 10
            pre = cur
            cur = cur.next
        return self.reverseList(head)

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
    head = "[1, 8, 9]"
    ans = solution.doubleIt(LeetCodeHelper.string_to_list_node(head))
    print(LeetCodeHelper.list_node_to_string(ans))
    pass
