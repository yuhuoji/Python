"""
739 每日温度
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-01-08 两种思路 尤其是从右到左

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 从左到右
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []
        for i, x in enumerate(temperatures):
            # 栈中元素递减 未找到下一个最大元素
            while stk and x > temperatures[stk[-1]]:
                j = stk.pop()
                ans[j] = i - j
            stk.append(i)
        return ans

    # 从右到左
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []
        # 从右到左 倒序遍历
        for i in range(n - 1, -1, -1):
            x = temperatures[i]
            # 栈中保存 可能成为下一个最大元素的数
            while stk and x >= temperatures[stk[-1]]:
                stk.pop()
            # 当前栈顶元素就是 x 的下一个最大元素
            if stk:
                ans[i] = stk[-1] - i
            stk.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
