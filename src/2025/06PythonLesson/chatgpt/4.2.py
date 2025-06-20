import numpy as np
import matplotlib.pyplot as plt

# SNR值
snr = [5, 10, 15]

# 对应频谱效率
eff_turbo_qpsk = [3.2, 4.8, 6.5]
eff_ldpc_256qam = [18.7, 28.5, 36.2]

# 设置字体和清晰度
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.family'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
plt.rcParams['axes.unicode_minus'] = False

# 绘图
bar_width = 0.3
x = np.arange(len(snr))

plt.figure(figsize=(10, 6))

# 绘制柱状图
plt.bar(x - bar_width/2, eff_turbo_qpsk, bar_width, label='Turbo + QPSK', color='lightgray', edgecolor='black')
plt.bar(x + bar_width/2, eff_ldpc_256qam, bar_width, label='LDPC + 256QAM', color='#4a7abc', edgecolor='black')

# 添加提升倍数标注
improvements = [5.8, 5.9, 5.6]
for i, txt in enumerate(improvements):
    plt.text(x[i] + bar_width/2, eff_ldpc_256qam[i] + 0.5, f'{txt:.1f}×', ha='center', fontsize=10, color='blue')

# 添加标签
plt.xlabel('信噪比 SNR (dB)', fontsize=14)
plt.ylabel('频谱效率 (bps/Hz)', fontsize=14)
plt.title('不同编码调制方案的频谱效率对比', fontsize=16, fontweight='bold')
plt.xticks(x, snr)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 去掉边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('spectral_efficiency_comparison_bar.png')
plt.show()
