"""
92 反转链表 II
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        # 拿到left上一个节点
        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # p0.next 是反转部分的尾节点
        p0.next.next = cur
        p0.next = pre
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    head = "[1,2,3,4,5]"
    ans = solution.reverseBetween(LeetCodeHelper.string_to_list_node(head), 2, 4)
    print(LeetCodeHelper.list_node_to_string(ans))
    pass
