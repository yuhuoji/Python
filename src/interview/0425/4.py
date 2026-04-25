import sys

"""
7
aaaaaaa
1 2
1 3
2 4
2 5
3 6
3 7
"""
"""
3
baa
1 2
1 3
"""
def solve():
    # 快速 I/O 读取所有输入数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    s = input_data[1]

    # 构建树的邻接表
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    # ID_map 用于映射 (父节点的 String ID, 当前字符) -> 唯一的 String ID
    ID_map = {}
    node_id = [0] * (n + 1)
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)

    order = []  # 记录从上到下的遍历顺序，用于后续无递归的自底向上合并
    depth[1] = 1

    # 1. 迭代式 DFS，确定父子关系、深度，并为每个节点分配唯一的 String ID
    stack = [1]
    visited = [False] * (n + 1)
    visited[1] = True

    while stack:
        u = stack.pop()
        order.append(u)

        # 计算当前节点的 String ID
        p_id = node_id[parent[u]] if parent[u] != 0 else 0
        char = s[u - 1]
        state = (p_id, char)

        if state not in ID_map:
            ID_map[state] = len(ID_map) + 1
        node_id[u] = ID_map[state]

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

    ans = [1] * (n + 1)
    # 存储每个节点对应的子树 String ID 集合
    node_set = [None] * (n + 1)

    # 为了快速查询某个 ID 代表的深度
    id_depth = [0] * (len(ID_map) + 1)
    for i in range(1, n + 1):
        id_depth[node_id[i]] = depth[i]

    # 2. 逆序遍历 order，实现自底向上的启发式合并 (DSU on Tree)
    for u in reversed(order):
        max_d = depth[u]  # 如果没有匹配，节点 u 的最大回文串就是自己，深度等于自身深度

        largest_child = -1
        max_size = -1

        # 寻找包含最多状态的“重儿子”
        for v in adj[u]:
            if v != parent[u]:
                if len(node_set[v]) > max_size:
                    max_size = len(node_set[v])
                    largest_child = v

        # 直接继承重儿子的集合 (引用传递，O(1) 复杂度)
        if largest_child != -1:
            u_set = node_set[largest_child]
        else:
            u_set = set()

        # 将“轻儿子”的集合合并进 u_set
        for v in adj[u]:
            if v != parent[u] and v != largest_child:
                for item_id in node_set[v]:
                    # 发现匹配！该 ID 存在于另外一棵子树中，LCA 就是当前节点 u
                    if item_id in u_set:
                        if id_depth[item_id] > max_d:
                            max_d = id_depth[item_id]
                    else:
                        u_set.add(item_id)

        # 加入当前节点 u 自身的 String ID
        u_set.add(node_id[u])
        node_set[u] = u_set

        # 题目中的路径点数等于 2 * 臂长 + 1
        ans[u] = 2 * (max_d - depth[u]) + 1

    # 输出结果
    print(" ".join(map(str, ans[1:])))


# --- 本地测试验证 ---
def local_test():
    import io
    test_cases = [
        # 示例 1
        ("7\naaaaaaa\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7", "5 3 3 1 1 1 1"),
        # 示例 2
        ("3\nbaa\n1 2\n1 3", "3 1 1")
    ]

    for i, (test_in, expected) in enumerate(test_cases, 1):
        print(f"--- 测试用例 {i} ---")
        sys.stdin = io.StringIO(test_in)
        print("预期输出:", expected)
        print("实际输出: ", end="")
        solve()
    sys.stdin = sys.__stdin__


if __name__ == '__main__':
    # 在判题平台上请将 local_test() 注释掉，只执行 solve()
    # local_test()
    solve()