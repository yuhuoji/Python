"""
5 5
0 0 0 0 0
1 2
1 3
2 4
2 5
2 1 4
1 1 3
2 4 1
1 2 5
2 5 1
"""

import sys
from collections import *


def function():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])

    val = [0] * (n + 1)
    for i, c in enumerate(data[2]):
        val[i + 1] = int(c)

    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    def get_path(start, end):
        q = deque([start])
        parent = {start: -1}

        while q:
            cur = q.popleft()
            if cur == end:
                break
            for nxt in adj[cur]:
                if nxt not in parent:
                    parent[nxt] = cur
                    q.append(nxt)

        path = []
        cur = end
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        return path[::-1]

    MOD = 10 ** 9 + 7

    result = []
    for _ in range(m):
        op, u, v = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3

        path = get_path(u, v)
        if op == 1:
            for node in path:
                val[node] ^= 1
        else:
            res = 0
            for node in path:
                res = (res * 2 + val[node]) % MOD
            result.append(str(res))

    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    function()
