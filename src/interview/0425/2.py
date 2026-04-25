import sys
import json
import numpy as np

"""
{"train":[[0,0],[1,0],[2,0],[3,1],[4,1],[5,1]],"test":[[-1],[2.5],[4]]}
[0, 0, 1]
"""
def solve():
    # 1. 数据读取
    input_str = sys.stdin.read().strip()
    # if not input_str:
    #     return

    try:
        data = json.loads(input_str)
    except json.JSONDecodeError:
        return

    train_data = np.array(data.get("train", []), dtype=float)
    test_data = np.array(data.get("test", []), dtype=float)

    if train_data.size == 0:
        print("[]")
        return

    X_train = train_data[:, :-1]
    y_train = train_data[:, -1].astype(int)

    N, M = X_train.shape

    # 总体正负样本数
    total_1 = np.sum(y_train == 1)
    total_0 = N - total_1

    best_G = float('inf')
    best_feat_idx = -1
    best_thresh = float('inf')

    epsilon = 1e-7

    # 2. 搜索过程
    for j in range(M):
        feat = X_train[:, j]

        # 稳定排序
        sort_idx = np.argsort(feat, kind='mergesort')
        feat_sorted = feat[sort_idx]
        y_sorted = y_train[sort_idx]

        # 候选 1: 最小值 - epsilon
        thresh = feat_sorted[0] - epsilon

        # 此时左子集为空，右子集包含所有数据
        g_L_term = 0.0
        g_R_term = (total_0 ** 2 + total_1 ** 2) / (N * N) if N > 0 else 0.0
        G = 1.0 - g_L_term - g_R_term

        # 更新最优（引入极小容差防止浮点数精度假并列）
        if G < best_G - 1e-12:
            best_G, best_feat_idx, best_thresh = G, j, thresh
        elif abs(G - best_G) <= 1e-12:
            if j < best_feat_idx:
                best_G, best_feat_idx, best_thresh = G, j, thresh
            elif j == best_feat_idx and thresh < best_thresh:
                best_G, best_feat_idx, best_thresh = G, j, thresh

        # 滑动统计左右子集
        n_L0, n_L1 = 0, 0
        n_R0, n_R1 = total_0, total_1

        for i in range(N - 1):
            if y_sorted[i] == 1:
                n_L1 += 1
                n_R1 -= 1
            else:
                n_L0 += 1
                n_R0 -= 1

            # 仅在相邻不同值中点设候选阈值
            if feat_sorted[i] != feat_sorted[i + 1]:
                thresh = (feat_sorted[i] + feat_sorted[i + 1]) / 2.0
                n_L = i + 1
                n_R = N - n_L

                # 计算加权 Gini
                g_L_term = (n_L0 ** 2 + n_L1 ** 2) / (N * n_L) if n_L > 0 else 0.0
                g_R_term = (n_R0 ** 2 + n_R1 ** 2) / (N * n_R) if n_R > 0 else 0.0
                G = 1.0 - g_L_term - g_R_term

                if G < best_G - 1e-12:
                    best_G, best_feat_idx, best_thresh = G, j, thresh
                elif abs(G - best_G) <= 1e-12:
                    if j < best_feat_idx:
                        best_G, best_feat_idx, best_thresh = G, j, thresh
                    elif j == best_feat_idx and thresh < best_thresh:
                        best_G, best_feat_idx, best_thresh = G, j, thresh

    # 3. 叶子预测值逻辑推断
    # 获取最佳划分下的左右子集标签
    left_mask = X_train[:, best_feat_idx] <= best_thresh
    right_mask = ~left_mask

    y_left = y_train[left_mask]
    y_right = y_train[right_mask]

    def get_leaf_pred(y_subset):
        if len(y_subset) == 0:
            return 0  # 子集为空，0/1数目相等（均为0），输出0
        c1 = np.sum(y_subset == 1)
        c0 = len(y_subset) - c1
        return 1 if c1 > c0 else 0

    pred_left = get_leaf_pred(y_left)
    pred_right = get_leaf_pred(y_right)

    # 4. 预测阶段
    preds = []
    if test_data.shape[0] > 0:
        test_feat = test_data[:, best_feat_idx]
        # np.where 完美贴合向量化输出逻辑
        preds = np.where(test_feat <= best_thresh, pred_left, pred_right).tolist()

    print(json.dumps(preds))


if __name__ == '__main__':
    solve()