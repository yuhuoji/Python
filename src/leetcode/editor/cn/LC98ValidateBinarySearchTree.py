"""
98 验证二叉搜索树
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-01-30

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 后序遍历 左右中
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf  # True
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            if l_max >= x or x >= r_min:
                return -inf, inf  # False
            return min(l_min, x), max(r_max, x)

        return dfs(root)[1] != inf


# 中序遍历
class Solution2:
    pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.pre >= root.val:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)


class Solution1:
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
