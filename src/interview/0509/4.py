"""
示例输入：
5,3,[1,2,3,4,5],[[3,4],[1,2],[5,2]],0

示例输出：
[4,3,2]
"""

from typing import List
import ast
import math


# 线段树 + 根号分治优化查询
class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr) - 1
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [0] * (size * 2)

        for i in range(1, self.n + 1):
            self.tree[size + i - 1] = arr[i]

        for i in range(size - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, pos: int, val: int) -> None:
        idx = self.size + pos - 1
        self.tree[idx] = val
        idx >>= 1

        while idx:
            self.tree[idx] = max(self.tree[idx << 1], self.tree[idx << 1 | 1])
            idx >>= 1

    def max_all(self) -> int:
        return self.tree[1]

    def find_first(self, left: int, right: int, need: int) -> int:
        if left > right or self.tree[1] < need:
            return -1
        return self._find_first(1, 1, self.size, left, right, need)

    def _find_first(self, node: int, l: int, r: int, ql: int, qr: int, need: int) -> int:
        if r < ql or qr < l or self.tree[node] < need:
            return -1

        if l == r:
            if l <= self.n:
                return l
            return -1

        mid = (l + r) >> 1

        res = self._find_first(node << 1, l, mid, ql, qr, need)
        if res != -1:
            return res

        return self._find_first(node << 1 | 1, mid + 1, r, ql, qr, need)

    def find_last(self, left: int, right: int, need: int) -> int:
        if left > right or self.tree[1] < need:
            return -1
        return self._find_last(1, 1, self.size, left, right, need)

    def _find_last(self, node: int, l: int, r: int, ql: int, qr: int, need: int) -> int:
        if r < ql or qr < l or self.tree[node] < need:
            return -1

        if l == r:
            if l <= self.n:
                return l
            return -1

        mid = (l + r) >> 1

        res = self._find_last(node << 1 | 1, mid + 1, r, ql, qr, need)
        if res != -1:
            return res

        return self._find_last(node << 1, l, mid, ql, qr, need)

    def collect_ge(self, left: int, right: int, need: int) -> List[int]:
        res = []
        self._collect_ge(1, 1, self.size, left, right, need, res)
        return res

    def _collect_ge(
            self,
            node: int,
            l: int,
            r: int,
            ql: int,
            qr: int,
            need: int,
            res: List[int]
    ) -> None:
        if r < ql or qr < l or self.tree[node] < need:
            return

        if l == r:
            if l <= self.n:
                res.append(l)
            return

        mid = (l + r) >> 1
        self._collect_ge(node << 1, l, mid, ql, qr, need, res)
        self._collect_ge(node << 1 | 1, mid + 1, r, ql, qr, need, res)


class Solution:
    def getMaxDistance(
            self,
            n: int,
            q: int,
            a: List[int],
            queries: List[List[int]],
            k: int
    ) -> List[int]:

        cnt = [0] * (n + 1)

        for x in a:
            if k == 0 or x != k:
                cnt[x] += 1

        seg = SegmentTree(cnt)

        block = int(math.sqrt(n)) + 2
        arr = [0] + a[:]

        def calc_distance(
                need_sum: int,
                left_l: int,
                left_r: int,
                right_l: int,
                right_r: int
        ) -> int:
            if left_l > left_r or right_l > right_r:
                return 0

            best = 0

            if need_sum <= block:
                for left_need in range(1, need_sum + 1):
                    right_need = max(1, need_sum - left_need)

                    left_pos = seg.find_first(left_l, left_r, left_need)
                    right_pos = seg.find_last(right_l, right_r, right_need)

                    if left_pos != -1 and right_pos != -1 and left_pos < right_pos:
                        best = max(best, right_pos - left_pos)

            else:
                high_need = (need_sum + 1) // 2

                high_left = seg.collect_ge(left_l, left_r, high_need)
                for left_pos in high_left:
                    right_need = max(1, need_sum - cnt[left_pos])
                    right_pos = seg.find_last(right_l, right_r, right_need)

                    if right_pos != -1 and left_pos < right_pos:
                        best = max(best, right_pos - left_pos)

                high_right = seg.collect_ge(right_l, right_r, high_need)
                for right_pos in high_right:
                    left_need = max(1, need_sum - cnt[right_pos])
                    left_pos = seg.find_first(left_l, left_r, left_need)

                    if left_pos != -1 and left_pos < right_pos:
                        best = max(best, right_pos - left_pos)

            return best

        def get_answer() -> int:
            max_cnt = seg.max_all()

            if max_cnt == 0:
                return 0

            left_max_pos = seg.find_first(1, n, max_cnt)
            right_max_pos = seg.find_last(1, n, max_cnt)

            # 情况 1：区间 [x, y] 覆盖所有最高频节点，只需要 cnt[x] + cnt[y] >= max_cnt
            ans1 = calc_distance(
                max_cnt,
                1,
                left_max_pos,
                right_max_pos,
                n
            )

            # 情况 2：区间 [x, y] 没有覆盖所有最高频节点，需要 cnt[x] + cnt[y] >= max_cnt + 1
            ans2 = calc_distance(
                max_cnt + 1,
                1,
                n,
                1,
                n
            )

            return max(ans1, ans2)

        ans = []

        for p, v in queries:
            old = arr[p]

            if k == 0 or old != k:
                cnt[old] -= 1
                seg.update(old, cnt[old])

            arr[p] = v

            if k == 0 or v != k:
                cnt[v] += 1
                seg.update(v, cnt[v])

            ans.append(get_answer())

        return ans


if __name__ == "__main__":
    raw = input().strip()

    n, q, a, queries, k = ast.literal_eval("(" + raw + ")")

    ret = Solution().getMaxDistance(n, q, a, queries, k)

    print(ret)
