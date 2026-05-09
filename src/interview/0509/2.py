"""
示例输入：
6,6,[5,7,9,11,14,16],[3,1,4,2,6,7],[[1,6],[1,7],[3,4],[4,3],[4,6],[4,7]],0

示例输出：
["YES","YES","YES","YES","NO","NO"]
"""

import ast
import bisect
from typing import List


class Solution:
    def solve(
            self,
            N: int,
            Q: int,
            c: List[int],
            t: List[int],
            plans: List[List[int]],
            k: int
    ) -> List[str]:

        limits = []

        # 题目说第 i 个采蜜点，i 从 1 开始
        for idx in range(N):
            i = idx + 1
            limit = c[idx] - t[idx] - k * i
            limits.append(limit)

        limits.sort()

        ans = []

        for y, start_time in plans:
            cannot_visit = bisect.bisect_right(limits, start_time)
            can_visit = N - cannot_visit

            if can_visit >= y:
                ans.append("YES")
            else:
                ans.append("NO")

        return ans


if __name__ == "__main__":
    raw = input().strip()

    N, Q, c, t, plans, k = ast.literal_eval("(" + raw + ")")

    ret = Solution().solve(N, Q, c, t, plans, k)

    print(str(ret).replace("'", '"'))