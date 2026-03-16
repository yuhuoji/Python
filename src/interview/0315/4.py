"""
2
5 2 3
5 7 6 4 5
4 4 4 4 4
6 2 2
10 1 10 1 10 1
0 0 0 0 0 0
"""
import sys


def solve():
    # 采用 sys 快速读取，应对笔试大数据量
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1
    out = []

    for _ in range(T):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        idx += 3

        # 业务需求 a
        a = [int(input_data[i]) for i in range(idx, idx + n)]
        idx += n
        # 基础容量 b
        b = [int(input_data[i]) for i in range(idx, idx + n)]
        idx += n

        # 计算每个点的基础容量缺口
        deficits = [a[i] - b[i] for i in range(n)]
        max_def = max(deficits)

        # 特判：如果本来基础容量就满足所有需求，不需要任何扩容包
        if max_def <= 0:
            out.append("0 0")
            continue

        # 贪心检验函数：在单包容量为 x 的情况下，最少需要多少个扩容包
        def check(x):
            packs = 0
            curr_expansion = 0
            # 差分数组，用于 O(1) 处理区间容量变化
            diff = [0] * (n + 1)

            for i in range(n):
                # 累加差分值，得到当前时间点的真实已扩容容量
                curr_expansion += diff[i]
                d = deficits[i]

                # 如果依然有缺口，说明必须在这里启动新包
                if d > curr_expansion:
                    needed = d - curr_expansion
                    # 向上取整计算需要几个容量为 x 的包
                    k = (needed + x - 1) // x
                    packs += k

                    # 提前剪枝：如果包数超过了限制的 m 个，说明当前 x 不可行
                    if packs > m:
                        return float('inf')

                    # 增加当前容量，并在过期时间点扣除
                    curr_expansion += k * x
                    if i + w <= n:
                        diff[i + w] -= k * x

            return packs

        # 特判：如果单包容量已经拉满到最大缺口，需要的包数仍然 > m，那彻底没戏了
        if check(max_def) > m:
            out.append("-1")
            continue

        # 二分查找最小的 x
        low = 1
        high = max_def
        ans_x = -1
        ans_c = -1

        while low <= high:
            mid = (low + high) // 2
            c = check(mid)
            if c <= m:
                # 当前容量可行，记录答案并尝试找更小的 x
                ans_x = mid
                ans_c = c
                high = mid - 1
            else:
                # 当前容量不可行，需要更大的 x
                low = mid + 1

        out.append(f"{ans_x} {ans_c}")

    # 一次性输出所有结果
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()