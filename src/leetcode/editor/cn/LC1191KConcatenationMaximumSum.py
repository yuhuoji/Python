"""
1191 K 次串联后最大子数组之和
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# 复用lc53
# 子数组可以为0

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 1_000_000_000 + 7
        if k == 1:
            return self.maxSubArray(arr)
        ans = self.maxSubArray(arr + arr)
        ans += max(sum(arr), 0) * (k - 2)
        return ans % MOD

    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0 # 字数组可以为0
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
