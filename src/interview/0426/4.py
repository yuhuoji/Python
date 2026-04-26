"""
测试用例可以直接复制以下内容在终端执行：

1
7 2
1 1 2 2 3 3

1
5 1
1 2 3 4
"""

import sys


def solve():
    # 采用一次性读取全部输入以达到最优的 I/O 性能
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1
    out = []

    for _ in range(T):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2

        # 处理边界情况
        if n == 1:
            out.append("0")
            continue

        # 1. 构建邻接表（树）
        children = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            p = int(input_data[idx])
            idx += 1
            children[p].append(i)

        # 2. 预处理出树的自底向上遍历顺序 (逆 BFS 序)
        # 用数组模拟队列，比 deque 稍快且无多余开销
        q = [1]
        ptr = 0
        while ptr < len(q):
            u = q[ptr]
            ptr += 1
            for c in children[u]:
                q.append(c)
        # 翻转即为自底向上遍历序列
        order = q[::-1]

        # 初始化 DP 数组，抽离在循环外减少内存分配开销
        dist = [-1] * (n + 1)

        # 贪心判断当前最大距离限制 D 下，需要的最小关键节点数量是否 <= k
        def check(D):
            keys_needed = 0

            # 每轮校验重置距离状态
            # dist 记录节点子树中"最深的未覆盖节点"距离当前节点的层数
            # 如果值为 -1，代表子树中所有节点均已被覆盖
            for i in range(1, n + 1):
                dist[i] = -1

            for u in order:
                max_child_dist = -1
                for c in children[u]:
                    if dist[c] > max_child_dist:
                        max_child_dist = dist[c]

                # 当前节点距离其子树中最深的未覆盖节点的距离
                cur_d = max_child_dist + 1

                # 如果距离达到了极限 D，必须在 u 放置关键节点 (根节点留到最后特判)
                if cur_d == D and u != 1:
                    keys_needed += 1
                    dist[u] = -1  # 放置后，自身及下方的节点全部视为已覆盖
                else:
                    dist[u] = cur_d

            # 根节点(1)特判：若向上走到根，仍有子树节点（或自身）未被覆盖，则必须把根设为关键节点
            if dist[1] >= 0:
                keys_needed += 1

            return keys_needed <= k

        # 3. 二分查找最小的合法距离 D
        low, high = 0, n - 1
        ans = n - 1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid  # 当前 D 够用，尝试更小的 D
                high = mid - 1
            else:
                low = mid + 1  # 覆盖失败，需要放宽（增大） D

        out.append(str(ans))

    # 快速统一输出
    print("\n".join(out))


if __name__ == '__main__':
    solve()