import datetime
import pandas as pd
import os

def process_excel(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 定义关键词列表和类型
    keywords = [
         '旅行'
    ]
    type = '生活购物'

    # 创建一个函数来检查文本是否包含任意关键词
    def contains_keyword(text):
        if isinstance(text, str):
            return any(keyword in text for keyword in keywords)
        return False

    # 创建掩码：对于 merged_category 为空且 cyber_star_name 或 description 中包含关键词的行，填入 '艺术文化'
    mask = (df['merged_category'].isna() | df['merged_category'].eq('')) & (
        df['cyber_star_name'].apply(contains_keyword) |
        df['description'].apply(contains_keyword) |
        df['user_name'].apply(contains_keyword)
    )
    df.loc[mask, 'merged_category'] = type

    # 统计处理完后的 merged_category 列为空的数量
    empty_count = df['merged_category'].isna().sum() + df['merged_category'].eq('').sum()

    # 获取当前日期和时间，格式化时间戳
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d_%H%M")

    # 生成新文件名并保存在原文件夹中
    new_file_name = f"updated_{formatted_time}_网红账号打标0705.xlsx"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    # 保存到新文件
    df.to_excel(new_file_path, index=False)

    print(f"处理完成。新文件保存为: {new_file_path}")
    print(f"merged_category 列为空的数量: {empty_count}")

# 使用示例
file_path = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0705/updated_1.3_网红账号打标0705.xlsx"
process_excel(file_path)