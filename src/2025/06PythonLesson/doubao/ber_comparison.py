import numpy as np
import matplotlib.pyplot as plt

# 报告中的误码率数据
snr_dB = np.arange(0, 16)
ber_ldpc = np.array([0.45, 0.38, 0.29, 0.21, 0.15, 0.09, 0.05, 0.023, 0.008, 0.002,
                    5e-4, 1e-4, 3e-5, 8e-6, 2e-6, 5e-7])
ber_turbo = np.array([0.48, 0.42, 0.35, 0.28, 0.22, 0.17, 0.13, 0.09, 0.06, 0.035,
                     0.018, 0.0087, 0.003, 0.0012, 5e-4, 2e-4])

# 设置图片清晰度和字体（关键：使用matplotlib内置的数学渲染）
plt.rcParams['figure.dpi'] = 300
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["text.usetex"] = False  # 禁用LaTeX，使用matplotlib内置渲染
plt.rcParams["mathtext.fontset"] = "cm"  # 使用Computer Modern字体（类似LaTeX）

# 绘制半对数坐标曲线
plt.figure(figsize=(10, 6))
plt.semilogy(snr_dB, ber_ldpc, 'o-', linewidth=2, markersize=8, markerfacecolor='blue',
             label='LDPC码', zorder=3)
plt.semilogy(snr_dB, ber_turbo, 's-', linewidth=2, markersize=8, markerfacecolor='red',
             label='Turbo码', zorder=3)

# 添加网格和标签（使用matplotlib内置的数学渲染）
plt.grid(axis='y', linestyle='--', zorder=0)
plt.xlabel('信噪比 SNR (dB)', fontsize=14)
plt.ylabel(r'误码率 BER ($10^x$)', fontsize=14)  # 数学符号使用$包裹
plt.title('LDPC码与Turbo码误码率性能对比', fontsize=16, fontweight='bold')
plt.legend(loc='best', fontsize=12)

# 突出显示关键数据点（使用matplotlib内置的数学渲染）
plt.plot(5, 2.3e-4, 'ro', markersize=10)
plt.plot(5, 8.7e-3, 'bo', markersize=10)
plt.text(5, 2.3e-4*1.5, r'LDPC: $2.3 \times 10^{-4}$', ha='center', va='bottom', fontsize=12)
plt.text(5, 8.7e-3*0.5, r'Turbo: $8.7 \times 10^{-3}$', ha='center', va='top', fontsize=12)

# 调整边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('ber_comparison_fixed.png', dpi=300)
plt.show()