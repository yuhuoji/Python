"""
24 两两交换链表中的节点
"""
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        p3 = p2.next
        # 两两交换
        p1.next = self.swapPairs(p3)
        p2.next = p1
        return p2

    # 迭代
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        while p0.next and p0.next.next:
            p1 = p0.next
            p2 = p1.next
            nxt = p2.next  # 保存下一组
            # 两两交换
            p0.next = p2
            p2.next = p1
            p1.next = nxt
            p0 = p1  # 准备下一组
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
