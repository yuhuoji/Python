"""
496 下一个更大元素 I
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-01-08 两种方向两种写法

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # 从右到左 栈中记录
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = {x: i for i, x in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stk = []
        n = len(nums2)
        for i in range(n - 1, -1, -1):
            x = nums2[i]
            while stk and x > stk[-1]:
                stk.pop()
            if stk and x in idx:
                ans[idx[x]] = stk[-1]
            stk.append(x)
        return ans

    # 从左到右 栈中记录还没计算出下一个最大元素的数
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = {x: i for i, x in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stk = []
        for i, x in enumerate(nums2):
            while stk and x > stk[-1]:
                ans[idx[stk.pop()]] = x
            if x in idx:
                stk.append(x)
        return ans

    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stk = []
        # 生成所有nums2的答案
        for i, x in enumerate(nums2):
            while stk and stk[-1] < x:
                mp[stk.pop()] = x
            stk.append(x)
        return [mp.get(x, -1) for x in nums1]
        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    ans = solution.nextGreaterElement(nums1, nums2)
    print(f"{ans}")
    pass
