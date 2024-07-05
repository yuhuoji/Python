import pandas as pd
import numpy as np
import os


def process_xls(file1_path, file2_path):
    # 读取文件1
    df1 = pd.read_excel(file1_path)

    # 读取文件2（映射关系）
    df2 = pd.read_excel(file2_path)

    # 创建映射字典
    mapping_dict = dict(zip(df2['现有标签'], df2['合并后标签']))

    # 获取所有有效的合并后标签
    valid_merged_labels = set(df2['合并后标签'])

    # 处理 category 列
    def map_category(x):
        if pd.isna(x):
            return np.nan

        # 处理多个类别的情况
        categories = [cat.strip() for cat in str(x).replace('、', '/').split('/')]

        for category in categories:
            # 检查完整的类别
            if category in mapping_dict and mapping_dict[category] in valid_merged_labels:
                return mapping_dict[category]

            # 检查子类别
            for key in mapping_dict:
                if key in category and mapping_dict[key] in valid_merged_labels:
                    return mapping_dict[key]

        # 如果没有匹配，返回 NaN
        return np.nan

    df1['merged_category'] = df1['category'].map(map_category)

    # 创建新文件名
    file1_name = os.path.basename(file1_path)
    new_file_name = f"updated_{file1_name}"
    new_file_path = os.path.join(os.path.dirname(file1_path), new_file_name)

    # 保存到新文件
    df1.to_excel(new_file_path, index=False)

    print(f"处理完成。新文件保存为: {new_file_path}")

# 使用示例
file1_path = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0705/网红账号打标0705.xlsx"
file2_path = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0705/MCN标签合并V2.xlsx"
process_xls(file1_path, file2_path)