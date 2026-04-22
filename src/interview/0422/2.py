import sys
import collections

# 如果需要导入额外的包或类，请在这里导入
# 定义二叉树节点结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level_order: list) -> TreeNode:
    """根据层序遍历数组构建二叉树"""
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = collections.deque([root])
    i = 1
    n = len(level_order)

    while queue and i < n:
        node = queue.popleft()

        # 构建左子节点
        if i < n and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        # 构建右子节点
        if i < n and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


def count_balanced_paths_logic(root: TreeNode) -> int:
    """核心算法：统计平衡路径的数量"""
    if not root:
        return 0

    # 哈希表记录前缀和出现的次数，初始化 0 出现 1 次
    prefix_counts = collections.defaultdict(int)
    prefix_counts[0] = 1

    total_zero_paths = 0  # 记录所有和为 0 的路径总数（包含长度为 1 的）
    zero_node_count = 0  # 记录单独值为 0 的节点数量

    def dfs(node: TreeNode, current_sum: int):
        nonlocal total_zero_paths, zero_node_count
        if not node:
            return

        # 统计单节点值为 0 的情况
        if node.val == 0:
            zero_node_count += 1

        current_sum += node.val

        # 如果当前前缀和在路径中出现过，说明存在和为 0 的子路径
        total_zero_paths += prefix_counts[current_sum]

        # 记录当前前缀和
        prefix_counts[current_sum] += 1

        # 向下递归遍历
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

        # 回溯：离开当前节点时，撤销当前前缀和记录，避免污染兄弟分支
        prefix_counts[current_sum] -= 1

    dfs(root, 0)

    # 最终结果：总符合条件的路径 - 长度为 1 的路径
    return total_zero_paths - zero_node_count

def func():
    raw_line = ""
    # 1. 死循环读取，过滤掉平台塞进来的所有前置空行
    while True:
        try:
            # 平台官方推荐的 input() 读法
            line = input().strip()
            if line:  # 只要读到了非空的内容
                raw_line = line
                break # 立刻跳出循环，开始处理
        except EOFError:
            return # 如果全是空行直接结束

    # 2. 暴力抹除中括号（已经证明有效）
    clean_line = raw_line.replace('[', '').replace(']', '')

    arr = []
    # 3. 解析为真正的数组
    if clean_line.strip():
        parts = clean_line.split(',')
        for p in parts:
            p = p.strip()
            if p == 'None' or p == 'null':
                arr.append(None)
            else:
                arr.append(int(p))

    # 4. 树构建与核心计算
    root = build_tree(arr)
    result = count_balanced_paths_logic(root)

    # 5. 唯一的一处标准输出
    print(result)


if __name__ == '__main__':

    func()
