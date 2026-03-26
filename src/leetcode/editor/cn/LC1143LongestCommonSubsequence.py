"""
1143 最长公共子序列
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if text1[i] == text2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
        return f[m][n]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
