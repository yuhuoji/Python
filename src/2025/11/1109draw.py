import matplotlib.pyplot as plt
import numpy as np

# 定义数据
demand_scale = np.arange(1, 1 + 0.5 * 11, 0.5)  # 从1开始，每个数据点增加0.5
my_algorithm = [100, 99.999, 100, 99.997, 99.996, 99.957, 99.927, 99.835, 99.548, 99.117, 99.741]
TEAVAR = [100, 99.998, 99.924, 99.729, 99.148, 98.241, 97.283, 96.127, 94.688, 93.607, 92.032]
FFC2 = [100, 99.998, 99.242, 96.484, 93.480, 90.405, 86.475, 81.747, 76.539, 71.0923, 65.586]
FFC1 = [100, 99.998, 99.991, 99.971, 99.941, 99.848, 99.631, 99.079, 97.997, 96.460, 93.549]
OPTR = [99.999, 99.995, 99.963, 99.882, 99.779, 99.579, 98.982, 98.063, 96.813, 94.818, 92.971]
ECMP = [100, 99.998, 98.939, 95.636, 92.359, 89.121, 84.956, 79.966, 74.284, 68.371, 62.440]

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 创建画布
plt.figure(figsize=(6, 4))

# 绘制各算法的可用性曲线
plt.plot(demand_scale, my_algorithm, marker='o', color='magenta', label='Telemark', linewidth=2)
plt.plot(demand_scale, FFC1, marker='D', color='navy', label='FFC1', linewidth=2)
plt.plot(demand_scale, OPTR, marker='*', color='teal', label='OPTR', linewidth=2)
plt.plot(demand_scale, TEAVAR, marker='s', color='lightgreen', label='TEAVAR', linewidth=2)
plt.plot(demand_scale, FFC2, marker='^', color='gold', label='FFC2', linewidth=2)
plt.plot(demand_scale, ECMP, marker='v', color='orange', label='ECMP', linewidth=2)

# 箭头两点坐标
x1, y1 = 1.5, 99.930    # ECMP的99.9%对应点
x2, y2 = 4.0, 99.930   # my_algorithm的99.927%对应点（x=4.0）

# ----------------------------------------------------
plt.annotate(
    '',               # 文本留空
    xy=(x1, y1),      # 箭头端点1
    xytext=(x2, y2),  # 箭头端点2
    arrowprops=dict(
        facecolor='blue',
        edgecolor='blue',
        linewidth=2,
        arrowstyle='<->,head_length=0.5,head_width=0.5',
        linestyle='-',
        shrinkA=5,
        shrinkB=5
    )
)

# 2. 再用 plt.text 单独在箭头中点下方添加文字
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
plt.text(
    mid_x,                # 中点x坐标
    mid_y - 0.02,         # 中点y坐标再往下偏移一点
    '2.5x more traffic',   # 你的文本
    ha='center',          # 水平居中
    va='top',             # 垂直对齐（顶部在 mid_y-0.02 处）
    fontsize=15,
    color='blue'
)

# ----------------------------------------------------

# 设置坐标轴标签和标题
plt.xlabel('Demand Scale')
plt.ylabel('Availability (%)')
# plt.title('不同算法在需求规模下的可用性对比')

# 调整坐标轴范围
plt.xlim(1, 5)
plt.ylim(98.95, 100.05)
plt.xticks(np.arange(1, 6))  # 强制显示x轴坐标：1,2,3,4,5

# 添加网格线（增强可读性）
plt.grid(True, linestyle='--', alpha=0.7)

# 显示图例
plt.legend(loc='lower left', fontsize=10, framealpha=0.9)

# 显示图形
plt.show()