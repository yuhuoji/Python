import warnings
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import numpy as np


# === 字体设置 ===
def setup_chinese_font():
    candidates = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'SimHei',
                  'Heiti TC', 'PingFang SC', 'Arial Unicode MS']
    available = {font.name for font in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in available:
            plt.rcParams['font.sans-serif'] = [name]
            plt.rcParams['axes.unicode_minus'] = False
            return name
    return "Default"


setup_chinese_font()


# === 关键：日期转换函数 ===
def convert_date(ym_float):
    """
    将 YYYY.MM 格式转换为线性时间轴
    例如:
    2024.02 (2月) -> 2024 + 1/12
    2024.12 (12月) -> 2024 + 11/12
    """
    year = int(ym_float)
    # 获取小数部分并乘以100转为月份整数 (0.12 -> 12, 0.02 -> 2)
    month_part = round((ym_float - year) * 100)

    if month_part == 0:
        return year  # 如果没有小数，就是年初

    # 转换为年的一小部分 (月份-1 / 12)
    return year + (month_part - 1) / 12


# === 数据 (注意：1-9月必须写成 .0x 格式) ===
data = {
    "GPT 系列": {
        2020: 2048,
        2022: 4096,
        2023: 32768,
        2023.11: 128000,  # GPT-4 Turbo (11月)
        2024.05: 128000,  # GPT-4o (5月)
        2025.02: 128_000,
        2025.09: 500_000,
    },
    "Claude 系列": {
        2023.03: 9000,  # Claude 1
        2023.07: 100000,  # Claude 2
        2024.03: 200_000,  # Claude 3
        2024.06: 200_000,  # Claude 3.5 Sonnet
        2024.10: 200_000,  # Claude 3.5 Haiku
        2025.05: 200_000,  # Claude 4.0(Opus/Sonnet)
        2025.09: 200_000,  # Claude 4.5 Sonnet
        2025.11: 1_000_000,  # Claude 4.5 0pus
    },
    "Gemini 系列": {
        2023.12: 32_000,  # Gemini 1.0 (12月)
        2024.02: 1_000_000,  # Gemini 1.5 Pro (2月，一定要写 .02)
        2024.12: 1_000_000,  # Gemini 2.0 Flash (12月，写 .12)
        2025.03: 1_000_000,
        2025.11: 1_000_000,
    },
    "DeepSeek 系列": {
        2023.11: 32768,  # V1
        2024.05: 128000,  # V2
        2025.01: 128_000,  # R1
        2025.03: 1_000_000,  # V3.1
        2025.12: 1_000_000,  # V3.2
    }
}

# === 标签位置 (同样使用 .0x 和 .xx 格式) ===
annotations = [
    # GPT
    (2020, 2048, "GPT-3 (2K)", (5, 20)),
    (2022, 4096, "GPT-3.5 (4K)", (0, -20)),
    (2023, 32768, "GPT-4\n(32K)", (-50, 20)),
    (2023.11, 128000, "GPT-4 Turbo\n(128K)", (-50, 30)),
    (2024.05, 128000, "GPT-4o\n(128K)", (20, 5)),
    (2025.02, 128000, "GPT-4.5\n(128K)", (60, -60)),
    (2025.09, 500000, "GPT-5.1\n(500K)", (20, -10)),

    # Claude
    (2023.03, 9000, "Claude 1 (9K)", (-10, -20)),
    (2023.07, 100000, "Claude 2\n(100K)", (-80, 10)),
    (2024.03, 200_000, "Claude 3\n(200K)", (-10, 10)),
    (2024.06, 200_000, "Claude 3.5 Sonnet\n(200K)", (-30, 70)),
    (2024.10, 200_000, "Claude 3.5 Haiku\n(200K)", (-30, 30)),
    (2025.05, 200_000, "Claude 4.0(0pus/Sonnet)\n(200K)", (30, 20)),
    (2025.09, 200_000, "Claude 4.5 Sonnet\n(200K)", (30, 0)),
    (2025.11, 1_000_000, "Claude 4.5 0pus\n(1M)", (10, 20)),

    # Gemini (现在顺序对了)
    (2023.12, 32_000, "Gemini 1.0\n(32K)", (30, -10)),
    (2024.02, 1_000_000, "Gemini 1.5 Pro\n(1M)", (-80, -10)),  # 2月
    (2024.12, 1_000_000, "Gemini 2.0 Flash\n(1M)", (-130, 30)),  # 12月
    (2025.03, 1_000_000, "Gemini 2.5 Pro\n(1M)", (-70, 25)),
    (2025.11, 1_000_000, "Gemini 3.0 Pro\n(1M)", (-80, 20)),

    # DeepSeek
    (2023.11, 32768, "DeepSeek V1\n(32K)", (-60, -60)),
    (2024.05, 128000, "DeepSeek V2\n(128K)", (-20, -50)),
    (2025.01, 128000, "DeepSeek R1\n(128K)", (-30, -50)),
    (2025.03, 1_000_000, "DeepSeek V3.1\n(1M)", (-30, -40)),
    (2025.12, 1_000_000, "DeepSeek V3.2\n(128K-1M)", (10, -30)),
]

# === 绘图 ===
fig, ax = plt.subplots(figsize=(14, 9))

styles = {
    "GPT 系列": {"color": "#d62728", "marker": "o", "ls": "-"},
    "Claude 系列": {"color": "#2ca02c", "marker": "s", "ls": "-"},
    "Gemini 系列": {"color": "#1f77b4", "marker": "^", "ls": "-."},
    "DeepSeek 系列": {"color": "#9467bd", "marker": "D", "ls": "--"}
}

# 绘制线条
for series_name, series_data in data.items():
    # 关键步骤：在这里调用 convert_date 处理 X 轴数据
    raw_years = list(series_data.keys())
    plot_years = [convert_date(y) for y in raw_years]  # 转换！

    windows = list(series_data.values())
    style = styles[series_name]

    ax.plot(plot_years, windows,
            marker=style["marker"], markersize=9, linewidth=3,
            label=series_name, color=style["color"], linestyle=style["ls"], alpha=0.9)

# 坐标轴设置
ax.set_yscale('log')
ax.set_ylim(800, 3500000)

yticks = [1000, 10000, 100000, 1000000]
yticklabels = ['1K', '10K', '100K', '1M']
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels, fontsize=12, fontweight='bold')

# X轴刻度
ax.set_xticks(range(2020, 2027))
ax.set_xticklabels(range(2020, 2027), fontsize=13)
ax.set_xlim(2019.8, 2026.5)

ax.set_title("主流大模型上下文窗口演进趋势 (2020-2025)", fontsize=22, fontweight='bold', pad=25)
ax.set_ylabel("上下文窗口大小 (Tokens)", fontsize=16, fontweight='bold')
ax.set_xlabel("年份", fontsize=14)

# 添加标注
for item in annotations:
    raw_year, window, text, offset = item

    # 关键步骤：标注的坐标也要转换
    real_x = convert_date(raw_year)

    color = 'black'
    for k, v in styles.items():
        if k.split(" ")[0] in text:
            color = v["color"]
            break

    ax.annotate(text,
                xy=(real_x, window),
                xytext=offset,
                textcoords='offset points',
                fontsize=11,
                color=color,
                fontweight='bold',
                arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5))

ax.legend(fontsize=12, loc='upper left', frameon=True, shadow=True)
ax.grid(True, which="major", ls="-", linewidth=0.8, alpha=0.3)
ax.grid(True, which="minor", ls=":", linewidth=0.5, alpha=0.2)

plt.tight_layout()
plt.show()
