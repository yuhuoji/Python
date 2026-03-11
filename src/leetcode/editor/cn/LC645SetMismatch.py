"""
645 错误的集合
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-03-11 元组解包计算顺序

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 桶排序
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, x in enumerate(nums):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:  # 使用元组解包交换错误
                y = nums[i] - 1
                nums[i], nums[y] = nums[y], nums[i]  # 错误代码 nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        ans = [-1, -1]
        for i, x in enumerate(nums):
            if x != i + 1:
                ans[0] = x
                ans[1] = i + 1
                break
        return ans

    def findErrorNums1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = [0] * (n + 1)
        for x in nums:
            cnt[x] += 1
        ans = [-1, -1]
        for i in range(1, n + 1):
            count = cnt[i]
            if count == 2:
                ans[0] = i
            if count == 0:
                ans[1] = i
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    input = [3, 2, 2]

    print(solution.findErrorNums(input))
    pass
