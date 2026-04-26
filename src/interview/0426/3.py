import sys
from collections import deque
"""
2 2
4
4 3 U
1 4 R
4 1 L
3 2 L
"""

def solve():
    # 采用一次性读取全部输入以达到最优的 I/O 性能
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    total_pieces = n * m
    # 使用定长数组替代哈希表，提升存取速度
    adj = [[] for _ in range(total_pieces + 1)]

    idx = 3
    for _ in range(k):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        d = input_data[idx + 2]
        idx += 3

        if d == 'U':
            adj[b].append((a, -1, 0))
            adj[a].append((b, 1, 0))
        elif d == 'B':
            adj[b].append((a, 1, 0))
            adj[a].append((b, -1, 0))
        elif d == 'L':
            adj[b].append((a, 0, -1))
            adj[a].append((b, 0, 1))
        elif d == 'R':
            adj[b].append((a, 0, 1))
            adj[a].append((b, 0, -1))

    # 记录每个节点的相对 x, y 坐标
    coords_x = [0] * (total_pieces + 1)
    coords_y = [0] * (total_pieces + 1)
    visited = [False] * (total_pieces + 1)

    # 从任意存在的节点开始 BFS，题目保证图是连通的，所以从 1 开始即可
    start_node = 1
    visited[start_node] = True
    q = deque([start_node])

    min_x = 0
    min_y = 0

    while q:
        curr = q.popleft()
        cx, cy = coords_x[curr], coords_y[curr]

        for nxt, dx, dy in adj[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                nx = cx + dx
                ny = cy + dy
                coords_x[nxt] = nx
                coords_y[nxt] = ny

                # 更新边界
                if nx < min_x: min_x = nx
                if ny < min_y: min_y = ny

                q.append(nxt)

    # 映射回真实的矩阵
    grid = [[0] * m for _ in range(n)]
    for i in range(1, total_pieces + 1):
        if visited[i]:
            grid[coords_x[i] - min_x][coords_y[i] - min_y] = i

    # 快速输出
    out = []
    for row in grid:
        out.append(" ".join(map(str, row)))
    print("\n".join(out))


if __name__ == '__main__':
    solve()
