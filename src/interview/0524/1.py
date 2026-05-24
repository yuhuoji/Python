"""
示例输入：
1 5
-0.04 -0.75 0.3 0.36 -0.07
0.5 -0.14 0.65 1.52 -0.23

示例输出：
0.46 -0.89 0.95 1.88 -0.3
"""

import numpy as np


def generate_data(noise, real):
    # 将输入的二维列表转成 numpy 数组，方便矩阵逐元素相加
    noise = np.array(noise)
    real = np.array(real)

    # 生成假数据：真实数据 + 随机噪声
    fake_data = real + noise

    # 返回生成后的数据
    return fake_data


if __name__ == '__main__':
    np.random.seed(42)

    # 输入样本数量 n 和特征维度 d
    n, d = map(int, input().split())

    # 输入 n 行随机噪声数据
    noise = [list(map(float, input().split())) for _ in range(n)]

    # 输入 n 行真实数据
    real_data = [list(map(float, input().split())) for _ in range(n)]

    # 调用函数生成假数据
    data = generate_data(noise, real_data)

    # 按要求输出，每个数字保留两位小数
    for row in data:
        print(' '.join(str(round(row[i], 2)) for i in range(d)))