"""
740 删除并获得点数
"""
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-23

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 转换为值域数组
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i, x in enumerate(nums):
            f[i] = max(x + f[i - 2], f[i - 1])
        return f[n - 1]

    def deleteAndEarn(self, nums: List[int]) -> int:
        a = [0] * (max(nums) + 1)
        for x in nums:
            a[x] += x
        return self.rob(a)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
