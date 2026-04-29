"""
5
1 2 3 4 5

对应输出
11100

5
5 2 7 3 2

对应输出
10000
"""

import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:n + 1]

    mx = max(a)
    ans = ['0'] * n

    m = 30 * n + 5
    son0 = [-1] * m
    son1 = [-1] * m
    tot = 1

    # 先插入最后一个数
    x = a[-1]
    p = 0
    for b in range(29, -1, -1):
        if (x >> b) & 1:
            np = son1[p]
            if np == -1:
                np = tot
                son1[p] = tot
                tot += 1
            p = np
        else:
            np = son0[p]
            if np == -1:
                np = tot
                son0[p] = tot
                tot += 1
            p = np

    for i in range(n - 2, -1, -1):
        x = a[i]

        # 查询 x 与右侧集合的最大异或值
        p = 0
        res = 0
        for b in range(29, -1, -1):
            bit = (x >> b) & 1
            if bit:
                np = son0[p]
                if np != -1:
                    res |= 1 << b
                    p = np
                else:
                    p = son1[p]
            else:
                np = son1[p]
                if np != -1:
                    res |= 1 << b
                    p = np
                else:
                    p = son0[p]

        if res >= mx:
            ans[i] = '1'

        # 插入 x
        p = 0
        for b in range(29, -1, -1):
            if (x >> b) & 1:
                np = son1[p]
                if np == -1:
                    np = tot
                    son1[p] = tot
                    tot += 1
                p = np
            else:
                np = son0[p]
                if np == -1:
                    np = tot
                    son0[p] = tot
                    tot += 1
                p = np

    sys.stdout.write(''.join(ans))


if __name__ == "__main__":
    solve()
