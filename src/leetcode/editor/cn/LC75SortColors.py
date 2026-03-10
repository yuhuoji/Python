"""
75 颜色分类
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *

# REVIEW @date 2026-03-09 荷兰国旗

"""
[0..i-1]有序 插入[i]
1. 插入2，只需a[i]=2
2. 插入1，a[p1]=1，p1++
3. 插入0，a[p0]=0，p0++，加上面所有步骤（将p1向后移动一位）

思考：0123怎么做
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left = cur = 0
        right = n - 1
        while cur <= right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:  # 2
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = 0
        for i, x in enumerate(nums):
            nums[i] = 2
            if x <= 1:
                nums[p1] = 1
                p1 += 1
            if x == 0:
                nums[p0] = 0
                p0 += 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
