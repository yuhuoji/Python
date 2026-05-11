"""
题目示例，可直接复制到终端输入：

示例1：
3,1,[[1,2]]

期望输出：
1

--------------------

示例2：
3,2,[[1,2],[2,3]]

期望输出：
0

--------------------

示例3：
4,4,[[1,2],[1,3],[1,4],[2,3]]

期望输出：
1
"""

from typing import List
import sys
import ast


class Solution:
    def solve(self, N: int, M: int, edges: List[List[int]]) -> int:
        full = (1 << N) - 1

        # g[i] 表示原图中 i 的邻接点集合
        g = [0] * N
        for a, b in edges:
            a -= 1
            b -= 1
            g[a] |= 1 << b
            g[b] |= 1 << a

        # miss[i] 表示原图中 i 没有连边的点
        miss = [0] * N
        for i in range(N):
            miss[i] = full ^ (1 << i) ^ g[i]

        # miss_cnt[mask]：mask 内部缺失边数量
        miss_cnt = [0] * (1 << N)
        size = [0] * (1 << N)

        for mask in range(1, 1 << N):
            lb = mask & -mask
            v = lb.bit_length() - 1
            rest = mask ^ lb

            size[mask] = size[rest] + 1
            miss_cnt[mask] = miss_cnt[rest] + (miss[v] & rest).bit_count()

        # 原图总缺失边数量
        total_missing = miss_cnt[full]

        # block_cost[mask]：
        # 如果 mask 作为一个“部”，同一部内部不能有边，所以已有边要删除。
        #
        # 最终总代价可以写成：
        # total_missing + sum(C(k,2) - 2 * miss_cnt[block])
        block_cost = [0] * (1 << N)

        for mask in range(1, 1 << N):
            k = size[mask]
            total_pairs = k * (k - 1) // 2
            block_cost[mask] = total_pairs - 2 * miss_cnt[mask]

        INF = 10 ** 18
        dp = [INF] * (1 << N)
        dp[0] = 0

        # dp[mask]：把 mask 中的点划分成若干个“部”的最小 block_cost 总和
        for mask in range(1, 1 << N):
            lb = mask & -mask

            sub = mask
            while sub:
                # 为避免重复划分，只枚举包含最低位点的 sub
                if sub & lb:
                    dp[mask] = min(
                        dp[mask],
                        block_cost[sub] + dp[mask ^ sub]
                    )

                sub = (sub - 1) & mask

        return total_missing + dp[full]


if __name__ == "__main__":
    raw = sys.stdin.read().strip()

    if not raw:
        sys.exit(0)

    # 支持平台样例输入：
    # 3,1,[[1,2]]
    try:
        N, M, edges = ast.literal_eval(raw)
    except Exception:
        # 也支持普通多行输入：
        # 3 1
        # 1 2
        nums = list(map(int, raw.replace(",", " ").split()))
        N, M = nums[0], nums[1]

        edges = []
        idx = 2
        for _ in range(M):
            edges.append([nums[idx], nums[idx + 1]])
            idx += 2

    print(Solution().solve(N, M, edges))