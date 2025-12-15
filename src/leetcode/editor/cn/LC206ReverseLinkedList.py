"""
206 反转链表
"""
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-15 迭代

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 递归
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        new_head = self.reverseList(cur.next)
        cur.next.next = cur
        cur.next = None
        return new_head

    # 迭代
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    name = "Leetcode ${question.frontendQuestionId}"
    print(f"s")
    solution = Solution()

    # 1. 准备数据 (直接复制 LeetCode 的输入字符串)
    input_str_1 = "[2,4,3]"
    input_str_2 = "[5,6,4]"

    # 2. 转换数据
    l1 = LeetCodeHelper.string_to_list_node(input_str_1)
    l2 = LeetCodeHelper.string_to_list_node(input_str_2)

    # 3. 运行解答
    result_node = solution.reverseList(l1)

    # 4. 打印结果
    print(LeetCodeHelper.list_node_to_string(result_node))
