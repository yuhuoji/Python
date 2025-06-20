import numpy as np
import matplotlib.pyplot as plt

# 报告中的频谱效率数据
snr = [5, 10, 15]
se_turbo = [3.2, 4.8, 6.5]  # Turbo+QPSK频谱效率（bps/Hz）
se_ldpc = [18.7, 28.5, 36.2]  # LDPC+256QAM频谱效率（bps/Hz）
improve_ratio = [5.8, 5.9, 5.6]  # 提升倍数

# 设置图片清晰度和字体
plt.rcParams['figure.dpi'] = 300
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

# 绘制柱状图
fig, ax1 = plt.subplots(figsize=(10, 6))
width = 0.35
x = np.arange(len(snr))

# 主坐标轴：绘制两种方案的频谱效率
bar1 = ax1.bar(x - width/2, se_turbo, width, label='Turbo+QPSK',
               color='lightgray', edgecolor='black', zorder=3)
bar2 = ax1.bar(x + width/2, se_ldpc, width, label='LDPC+256QAM',
               color='skyblue', edgecolor='black', zorder=3)

# 次坐标轴：绘制提升倍数
ax2 = ax1.twinx()
bar3 = ax2.bar(x, improve_ratio, width*0.4, label='提升倍数',
               color='salmon', alpha=0.7, edgecolor='black', zorder=3)
ax2.set_ylabel('提升倍数', fontsize=12)
ax2.set_ylim(0, max(improve_ratio)*1.1)

# 添加标签和标题
ax1.set_xlabel('信噪比 SNR (dB)', fontsize=14)
ax1.set_ylabel('频谱效率 (bps/Hz)', fontsize=14)
ax1.set_title('不同SNR下频谱效率对比', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(snr)
ax1.grid(axis='y', linestyle='--', zorder=0)

# 添加数据标签函数
def add_labels(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(bar1, ax1)
add_labels(bar2, ax1)
add_labels(bar3, ax2)

# 添加图例
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 调整边框
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('spectral_efficiency.png')
plt.show()