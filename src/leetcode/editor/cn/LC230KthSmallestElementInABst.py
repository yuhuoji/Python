"""
230 二叉搜索树中第 K 小的元素
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal k
            if not node or k < 0:
                return -1
            left_res = dfs(node.left)
            if left_res != -1:
                return left_res
            k -= 1
            if k == 0:
                return node.val
            return dfs(node.right)

        return dfs(root)

    # 外部变量 nonlocal
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        res = -1

        def dfs(node: Optional[TreeNode]):
            nonlocal k, res
            if not node or k < 0:
                return
            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val
            dfs(node.right)

        dfs(root)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
