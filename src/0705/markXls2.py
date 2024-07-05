import pandas as pd
import numpy as np
import os


def process_excel(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 定义关键词列表
    keywords = ['传媒', '地产', '房产', '家庭', '教育', '金融', '军事', '科技', '科普', '科学',
                '历史', '媒体', '评测种草', '人文', '人物', '企业', '商业', '时事', '时政',
                '数码', '新闻', '原创', '战术', '杂志', '职场', '财经', '政治']

    # 创建一个函数来检查是否包含关键词
    def contains_keyword(text):
        if isinstance(text, str):
            return any(keyword in text for keyword in keywords)
        return False

    # 对于 merged_category 为空且 cyber_star_name 包含关键词的行，填入 "社会时政"
    mask = (df['merged_category'].isna() | df['merged_category'].eq('')) & df['cyber_star_name'].apply(contains_keyword)
    df.loc[mask, 'merged_category'] = '社会时政'

    # 创建新文件名
    file_name = os.path.basename(file_path)
    new_file_name = f"updated_1.2_{file_name}"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    # 保存到新文件
    df.to_excel(new_file_path, index=False)

    print(f"处理完成。新文件保存为: {new_file_path}")


# 使用示例
file_path = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0705/updated_1.1_网红账号打标0705.xlsx"
process_excel(file_path)