import matplotlib.pyplot as plt
import numpy as np

# 定义数据
x = np.array([1, 2, 3])  # Top1, Top2, Top3
labels = ['Top1', 'Top2', 'Top3']
DagFusion = np.array([60, 68, 72])
TVDIag = np.array([65, 72, 75])
Ours = np.array([70, 78, 82])

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线
ax.plot(x, DagFusion, marker='o', linestyle='--', color='blue', label='DagFusion')
ax.plot(x, TVDIag, marker='s', linestyle=':', color='green', label='TVDIag')
ax.plot(x, Ours, marker='^', linestyle='-', color='red', linewidth=2, label='Ours')

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels)

# 设置 y 轴范围
ax.set_ylim(40, 85)

# 添加标题和轴标签
ax.set_title('故障定位预测排序')
ax.set_xlabel('故障定位预测排序')
ax.set_ylabel('定位准确率(%)')

# 添加图例
ax.legend()

# 显示图形
plt.show()