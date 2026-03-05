"""
3158 求出出现两次数字的 XOR 值
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = vis = 0
        for x in nums:
            if vis >> x & 1:
                ans ^= x
            else:
                vis = vis | (1 << x)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
