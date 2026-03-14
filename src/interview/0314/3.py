"""
5 5 5
1 2
1 5
3 5
2 4
1 3
2 4
1 1
2 2
1 2
2 1

"""
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        edges.append((u, v))

    ops = []
    del_edges = [False] * m  # 标记要删除的边
    deg = [0] * (n + 1)      # 初始度数
    for i in range(m):
        u, v = edges[i]
        deg[u] += 1
        deg[v] += 1

    for _ in range(q):
        op = int(data[idx]); idx += 1
        x = int(data[idx]); idx += 1
        ops.append((op, x))
        if op == 1:
            del_edges[x-1] = True
            u, v = edges[x-1]
            deg[u] -= 1  # 删边后度数减少
            deg[v] -= 1

    # 并查集：维护父节点 + 连通块最大权值
    parent = list(range(n + 1))
    max_val = [i + deg[i] for i in range(n + 1)]  # 初始权值 = 编号 + 度数

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]  # 路径压缩
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        parent[v_root] = u_root
        if max_val[v_root] > max_val[u_root]:
            max_val[u_root] = max_val[v_root]

    # 构建最终状态：只保留未被删除的边
    for i in range(m):
        if not del_edges[i]:
            union(edges[i][0], edges[i][1])

    # 逆序处理操作：删边 → 加边（恢复度数 + 合并）
    ans = []
    for op, x in reversed(ops):
        if op == 1:
            u, v = edges[x-1]
            deg[u] += 1
            deg[v] += 1
            # 更新权值（因为度数恢复了）
            max_val[find(u)] = max(max_val[find(u)], u + deg[u])
            max_val[find(v)] = max(max_val[find(v)], v + deg[v])
            union(u, v)
        else:
            root = find(x)
            ans.append(str(max_val[root]))

    # 倒序输出结果
    print('\n'.join(reversed(ans)))

if __name__ == "__main__":
    main()