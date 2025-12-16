"""
25 K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        # 拿到总长度
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        n = cnt
        p0 = dummy
        # k个一组反转
        while cnt - k >= 0:
            cnt -= k
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            next_p0 = p0.next  # 下一组的上一个节点
            p0.next.next = cur
            p0.next = pre
            p0 = next_p0  # 准备下一组的上一个节点

        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
