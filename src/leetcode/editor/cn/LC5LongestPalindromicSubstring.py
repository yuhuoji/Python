"""
5 最长回文子串
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# TODO @date 2026-03-16
# REVIEW @date 2026-03-16 Manacher 算法

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 方法二：Manacher 算法
    # s->t
    # ti = 2si + 2
    # si = ti/2 - 1
    # halfLen

    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('^' + s + '$')

        pass

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0
        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开
        return s[ans_left:ans_right]

    # 中心扩散法
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开
        return s[ans_left:ans_right]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
