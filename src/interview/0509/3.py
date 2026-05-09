"""
示例1输入：
3,2,"111",[[1,2],[1,3]]

示例1输出：
[3,1,0]

示例2输入：
3,2,"000",[[1,2],[1,3]]

示例2输出：
[3,0,0]

示例3输入：
7,8,"1101101",[[6,2],[1,2],[2,3],[6,3],[1,3],[1,7],[4,5],[2,7]]

示例3输出：
[11,7,4,2,1,1,0]
"""

import ast
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

        # cnt[x] 表示 x 所在连通块中，当前真正在线、需要计数的节点数量
        self.cnt = [0] * (n + 1)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> int:
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return 0

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        # 两个连通块合并后，新增加的可达点对数量
        delta = self.cnt[ra] * self.cnt[rb]

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.cnt[ra] += self.cnt[rb]

        return delta

    def activate(self, x: int) -> int:
        """
        把节点 x 变成真实在线节点。
        如果当前连通块里已有 c 个真实节点，则新增 c 对可达点对。
        """
        root = self.find(x)
        delta = self.cnt[root]
        self.cnt[root] += 1
        return delta


class Solution:
    def getReachablePairs(
        self,
        n: int,
        m: int,
        s: str,
        edges: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dsu = DSU(n) # 你眼瘸吗 你这什么缩紧？

        # available[i] 表示节点 i 当前是否已经在并查集中
        # s[i - 1] == '1' 的点，一开始作为“透明中转点”加入
        available = [False] * (n + 1)

        for i in range(1, n + 1):
            if s[i - 1] == '1':
                available[i] = True

        current_pairs = 0

        # 先合并所有透明节点之间的边
        for u, v in edges:
            if available[u] and available[v]:
                current_pairs += dsu.union(u, v)

        ans = [0] * n

        # 逆序恢复节点
        for i in range(n, 0, -1):
            if not available[i]:
                available[i] = True

                for nxt in graph[i]:
                    if available[nxt]:
                        current_pairs += dsu.union(i, nxt)

            # 当前节点 i 变成真实在线节点，计入答案
            current_pairs += dsu.activate(i)

            ans[i - 1] = current_pairs

        return ans


if __name__ == "__main__":
    raw = input().strip()

    n, m, s, edges = ast.literal_eval("(" + raw + ")")

    ret = Solution().getReachablePairs(n, m, s, edges)

    print(ret)