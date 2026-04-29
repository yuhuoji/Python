"""
3
0 2
4 4
6 10
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input().strip())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    intervals.sort()

    ans = 0
    for l, r in intervals:
        if r < ans:
            continue
        if l > ans:
            break
        ans = max(ans, r + 1)

    print(ans)


if __name__ == "__main__":
    solve()
