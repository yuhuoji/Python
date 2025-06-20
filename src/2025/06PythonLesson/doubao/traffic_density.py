import numpy as np
import matplotlib.pyplot as plt

# 报告4.3节中的流量密度数据
scenarios = ['城市宏蜂窝', '密集城区', '室内热点']
measured = [5.4, 6.8, 8.1]  # 实测流量密度(Mbps/m²)
simulated = [7.2, 8.7, 10.5]  # 仿真流量密度(Mbps/m²)
error_rate = [(7.2-5.4)/5.4*100, (8.7-6.8)/6.8*100, (10.5-8.1)/8.1*100]  # 误差率(%)

# 图表参数设置
plt.rcParams['figure.dpi'] = 300  # 图片清晰度
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]  # 中文字体
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

# 绘制图表
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = np.arange(len(scenarios))

# 绘制实测值和仿真值柱状图
bar1 = ax.bar(x - bar_width/2, measured, bar_width,
              label='实测值', color='#f0f0f0', edgecolor='black', zorder=3)
bar2 = ax.bar(x + bar_width/2, simulated, bar_width,
              label='仿真值', color='#a6cee3', edgecolor='black', zorder=3)

# 添加误差率标签
for i, err in enumerate(error_rate):
    ax.text(x[i], max(measured[i], simulated[i]) + 0.4,
            f'{err:.1f}%', ha='center', va='bottom',
            fontsize=10, fontweight='bold', color='#e31a1c')

# 添加标签和标题
ax.set_xlabel('场景', fontsize=14)
ax.set_ylabel('流量密度 (Mbps/m²)', fontsize=14)
ax.set_title('不同场景下实测与仿真流量密度对比', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(scenarios)
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
ax.legend(loc='upper left', fontsize=12)

# 美化图表（移除多余边框）
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 调整y轴范围，为误差率标签留出空间
ax.set_ylim(0, max(simulated) * 1.15)

plt.tight_layout()
plt.savefig('traffic_density_comparison.png', dpi=300)
plt.show()