import numpy as np
import matplotlib.pyplot as plt

# 报告中的流量密度数据
scenarios = ['城市宏蜂窝', '密集城区', '室内热点']
measured = [5.4, 6.8, 8.1]       # 实测流量密度（Mbps/m²）
simulated = [7.2, 8.7, 10.5]     # 仿真流量密度（Mbps/m²）
error_rate = [(7.2-5.4)/5.4*100, (8.7-6.8)/6.8*100, (10.5-8.1)/8.1*100]  # 误差率（%）

# 设置图片清晰度和字体
plt.rcParams['figure.dpi'] = 300
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

# 绘制分组柱状图
plt.figure(figsize=(10, 6))
bar_width = 0.3
x = np.arange(len(scenarios))

# 绘制实测值和仿真值柱状图
bar1 = plt.bar(x - bar_width/2, measured, bar_width, label='实测值',
              color='lightgray', edgecolor='black', zorder=3)
bar2 = plt.bar(x + bar_width/2, simulated, bar_width, label='仿真值',
              color='lightblue', edgecolor='black', zorder=3)

# 添加误差率标签
for i, err in enumerate(error_rate):
    plt.text(x[i], simulated[i] + 0.5, f'{err:.1f}%',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# 添加标签和标题
plt.xlabel('场景', fontsize=14)
plt.ylabel('流量密度 (Mbps/m²)', fontsize=14)
plt.title('实测与仿真流量密度对比', fontsize=16, fontweight='bold')
plt.xticks(x, scenarios)
plt.grid(axis='y', linestyle='--', zorder=0)
plt.legend(loc='best', fontsize=12)

# 调整边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('traffic_density.png')
plt.show()