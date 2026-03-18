"""
10 3
0.5 0.3 0.4 0
0.6 0.2 0.5 0
0.4 0.3 0.3 0
0.7 0.4 0.6 0
2.1 2.3 2.2 1
2.3 2.2 2.4 1
2.2 2.4 2.3 1
4.5 4.3 4.4 2
4.4 4.5 4.6 2
4.6 4.4 4.5 2
2.2 2.1 2.3
"""

import sys
from collections import Counter

def solve():
    # 读取所有输入，按行分割，过滤掉空行
    input_lines = [line.strip() for line in sys.stdin.read().split('\n') if line.strip()]
    if not input_lines:
        return

    # 1. 解析 N 和 K
    first_line = input_lines[0].split()
    N = int(first_line[0])
    K = int(first_line[1])

    # 2. 解析训练数据 (第 2 行 到 第 N+1 行)
    train_data = []
    for i in range(1, N + 1):
        parts = input_lines[i].split()
        # 前面部分是特征向量，最后一个数字是标签 (类别)
        features = tuple(float(x) for x in parts[:-1])
        label = int(float(parts[-1]))
        train_data.append((features, label))

    # 3. 解析待分类的语音特征向量 (最后一行)
    target_parts = input_lines[N + 1].split()
    target_vec = tuple(float(x) for x in target_parts)

    # 4. 计算所有训练样本与目标向量的“距离平方”
    distances = []
    for features, label in train_data:
        # 使用生成器表达式计算距离平方和，省略开方操作以提升性能
        dist_sq = sum((x - y) ** 2 for x, y in zip(features, target_vec))
        distances.append((dist_sq, label))

    # 5. 根据距离平方进行升序排序
    distances.sort(key=lambda x: x[0])

    # 6. 获取距离最近的 K 个邻居的标签
    top_k_labels = [label for _, label in distances[:K]]

    # 7. 统计出现次数最多的类别
    label_counts = Counter(top_k_labels)
    # most_common(1) 返回格式如 [(label, count)]
    predicted_label = label_counts.most_common(1)[0][0]

    # 输出结果
    print(predicted_label)


if __name__ == '__main__':
    solve()