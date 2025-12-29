"""
1015 可被 K 整除的最小整数
"""
from itertools import count
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-29 解法2

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        x = 1 % k
        for i in count(1):
            if x == 0:
                return i
            x = (x * 10 + 1) % k

    def smallestRepunitDivByK1(self, k: int) -> int:
        seen = set()
        x = 1
        while x and x not in seen:
            seen.add(x)
            x = (x * 10 + 1) % k
        return -1 if x else len(seen) + 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
