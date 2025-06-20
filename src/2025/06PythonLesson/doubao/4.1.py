import numpy as np
import matplotlib.pyplot as plt

# 报告中的误码率数据
snr_dB = np.arange(0, 16)  # 0到15dB
ber_ldpc = np.array([0.45, 0.38, 0.29, 0.21, 0.15, 0.09, 0.05, 0.023, 0.008, 0.002,
                    5e-4, 1e-4, 3e-5, 8e-6, 2e-6, 5e-7])
ber_turbo = np.array([0.48, 0.42, 0.35, 0.28, 0.22, 0.17, 0.13, 0.09, 0.06, 0.035,
                     0.018, 0.0087, 0.003, 0.0012, 5e-4, 2e-4])

# 设置图片清晰度和字体
plt.rcParams['figure.dpi'] = 300
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]  # 中文字体
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

# 绘制半对数坐标曲线
plt.figure(figsize=(10, 6))
plt.semilogy(snr_dB, ber_ldpc, 'o-', linewidth=2, markersize=8, markerfacecolor='blue',
             markeredgecolor='blue', label='LDPC码', zorder=3)
plt.semilogy(snr_dB, ber_turbo, 's-', linewidth=2, markersize=8, markerfacecolor='red',
             markeredgecolor='red', label='Turbo码', zorder=3)

# 添加网格和标签
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
plt.xlabel('信噪比 SNR (dB)', fontsize=14)
plt.ylabel('误码率 BER', fontsize=14)
plt.title('LDPC码与Turbo码误码率性能对比', fontsize=16, fontweight='bold')
plt.legend(loc='best', fontsize=12)

# 突出显示报告中提到的关键数据点（SNR=5dB）
key_snr = 5
key_ber_ldpc = 2.3e-4
key_ber_turbo = 8.7e-3

# 绘制标记点
plt.plot(key_snr, key_ber_ldpc, 'ro', markersize=10, zorder=4)
plt.plot(key_snr, key_ber_turbo, 'bo', markersize=10, zorder=4)

# 添加数据标签（使用科学计数法，避免LaTeX渲染）
ldpc_label = f'LDPC: {key_ber_ldpc:.1e}'
turbo_label = f'Turbo: {key_ber_turbo:.1e}'

plt.text(key_snr, key_ber_ldpc * 1.5, ldpc_label,
         ha='center', va='bottom', fontsize=12, color='blue')
plt.text(key_snr, key_ber_turbo * 0.5, turbo_label,
         ha='center', va='top', fontsize=12, color='red')

# 调整边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# 设置x轴刻度标签旋转45度
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('ber_comparison.png', dpi=300)
plt.show()