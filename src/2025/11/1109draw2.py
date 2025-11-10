import matplotlib.pyplot as plt
import numpy as np

# 定义数据
demand_scale = np.arange(1, 1 + 0.5 * 11, 0.5)  # 从1开始，每个数据点增加0.5
my_algorithm = [100, 99.989, 99.983, 100, 100, 99.999, 100, 99.587, 99.765, 99.775, 99.656]
TEAVAR = [100, 99.994, 99.938, 99.751, 99.503, 99.227, 98.856, 98.355, 98.193, 97.647, 97.129]
FFC2 = [100, 99.414, 97.191, 95.090, 92.702, 89.384, 85.643, 82.309, 77.768, 73.136, 68.046]
FFC1 = [100, 99.999, 99.997, 99.986, 99.970, 99.950, 99.915, 99.881, 99.819, 99.746, 99.648]
OPTR = [100, 100, 100, 99.999, 99.998, 99.989, 99.939, 99.827, 99.632, 99.411, 99.225]
ECMP = [99.927, 97.663, 94.613, 90.555, 86.109, 81.907, 77.611, 73.737, 67.897, 63.246, 57.633]

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


# ----------------------------------------------------
# ----------------------------------------------------
# 箭头两点坐标
x1, y1 = 1.0, 99.8    # <-- ***修改点***：将 x1 从 0.3 改为 1.0
x2, y2 = 4.3, 99.8   # my_algorithm的99.927%对应点（x=4.0）
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
    '4x more traffic',  # <-- ***提示***：(4.3 - 1.0) = 3.3
    ha='center',          # 水平居中
    va='top',             # 垂直对齐（顶部在 mid_y-0.02 处）
    fontsize=15,
    color='blue'
)
# ----------------------------------------------------

# ----------------------------------------------------

# 设置坐标轴标签和标题
plt.xlabel('Demand Scale')
plt.ylabel('Availability (%)')
# plt.title('不同算法在需求规模下的可用性对比')

# 调整坐标轴范围
plt.xlim(1, 6)
plt.ylim(98.95, 100.05)
plt.xticks(np.arange(1, 7))  # 强制显示x轴坐标：1,2,3,4,5

# 添加网格线（增强可读性）
plt.grid(True, linestyle='--', alpha=0.7)

# 显示图例
plt.legend(loc='lower left', fontsize=10, framealpha=0.9)

# 显示图形
plt.show()