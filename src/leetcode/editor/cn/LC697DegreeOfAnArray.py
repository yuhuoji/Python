"""
697 数组的度
"""
import collections
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# collections.Counter() 使用

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = {}, {}
        cnt = collections.Counter()
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            cnt[x] += 1
        degree = max(cnt.values())
        ans = len(nums)
        for k, v in cnt.items():
            if v == degree:
                ans = min(ans, right[k] - left[k] + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
