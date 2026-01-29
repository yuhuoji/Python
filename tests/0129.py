# 1.有序数组的二分查找
# 2.二叉搜索树找第 k 大的元素
# 1 - 10 k = 3 返回8 k = 4 返回7
from typing import *
from src.leetcode.lc_utils import *


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def searchTree(root: Optional[TreeNode], k: int) -> Optional[int]:
    res = None

    def dfs(node: Optional[TreeNode]) -> None:
        nonlocal k, res
        if not node or k == 0:
            return
        # 右
        dfs(node.right)
        if k == 0:
            return
        k -= 1
        if k == 0:
            res = node.val
            return
        # 左
        dfs(node.left)

    dfs(root)
    return res


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    # print(solution.search(nums, target))

    root = "[5, 3, 6, 2, 4, null, null, 1]"
    k = 3

    ans = searchTree(LeetCodeHelper.string_to_tree_node(root), k)
    print(ans)
