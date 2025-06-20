import numpy as np
import matplotlib.pyplot as plt

# 报告中的频谱效率数据
snr = [5, 10, 15]
se_turbo = [3.2, 4.8, 6.5]     # Turbo+QPSK频谱效率（bps/Hz）
se_ldpc = [18.7, 28.5, 36.2]   # LDPC+256QAM频谱效率（bps/Hz）
improve_ratio = [5.8, 5.9, 5.6] # 提升倍数

# 设置图片清晰度和字体
plt.rcParams['figure.dpi'] = 300
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

# 绘制柱状图（增加宽度避免重叠）
fig, ax1 = plt.subplots(figsize=(12, 7))
width = 0.32
x = np.arange(len(snr))

# 绘制Turbo+QPSK和LDPC+256QAM的频谱效率
bar1 = ax1.bar(x - width, se_turbo, width, label='Turbo+QPSK',
               color='lightgray', edgecolor='black', zorder=3)
bar2 = ax1.bar(x + width, se_ldpc, width, label='LDPC+256QAM',
               color='skyblue', edgecolor='black', zorder=3)

# 次坐标轴：绘制提升倍数（调整位置和宽度）
ax2 = ax1.twinx()
bar3 = ax2.bar(x, improve_ratio, width*0.5, label='提升倍数',
               color='salmon', alpha=0.7, edgecolor='black', zorder=3)
ax2.set_ylabel('提升倍数', fontsize=12)
ax2.set_ylim(0, max(improve_ratio) * 1.2)  # 扩展y轴范围

# 添加标签和标题
ax1.set_xlabel('信噪比 SNR (dB)', fontsize=14)
ax1.set_ylabel('频谱效率 (bps/Hz)', fontsize=14)
ax1.set_title('不同SNR下频谱效率对比', fontsize=16, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(snr)
ax1.grid(axis='y', linestyle='--', zorder=0)

# 添加数据标签（优化位置）
def add_labels(bars, ax, offset_y=0, offset_text=0):
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height + offset_y),
                    xytext=(0, offset_text),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

add_labels(bar1, ax1, offset_y=0.2, offset_text=3)   # Turbo+QPSK标签上移
add_labels(bar2, ax1, offset_y=0.2, offset_text=3)   # LDPC+256QAM标签上移
add_labels(bar3, ax2, offset_y=0.1, offset_text=5)  # 提升倍数标签上移

# 添加图例
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

# 调整边框
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('spectral_efficiency.png', dpi=300)
plt.show()