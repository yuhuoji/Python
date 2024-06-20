import pandas as pd
import csv
import re

# 文件路径
csv_file_path = 'C:/Users/yuhuo/Documents/Document/6.17-21/6.20/图谱人物数据.csv'
encoded_csv_file_path = 'C:/Users/yuhuo/Documents/Document/6.17-21/6.20/图谱人物数据_utf8.csv'
cleaned_csv_file_path = 'C:/Users/yuhuo/Documents/Document/6.17-21/6.20/图谱人物数据_clean.csv'

# 读取 CSV 文件
try:
    df = pd.read_csv(csv_file_path, encoding='utf-8')
    print("CSV文件读取成功.")
except Exception as e:
    print(f"读取CSV文件时发生错误: {str(e)}")
    exit()

# 定义函数：处理 resume 列中的换行符 \n
def clean_resume(text):
    try:
        if isinstance(text, str):
            return re.sub(r'\s*\n\s*', ' ', text.strip())  # 将 \n 替换为 空格，并去除多余空格
        return text
    except Exception as e:
        print(f"处理文本时发生错误: {str(e)}")
        return text

# 逐行处理 resume 列中的每个单元格
try:
    df['resume'] = df['resume'].apply(clean_resume)
    print("resume列处理完成.")
except Exception as e:
    print(f"处理resume列时发生错误: {str(e)}")
    exit()

# 删除单元格内容前后的空白空格
try:
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    print("删除单元格前后空白完成.")
except Exception as e:
    print(f"删除单元格前后空白时发生错误: {str(e)}")
    exit()

# 获取每个单元格的字符串长度
string_lengths = df.applymap(lambda x: len(str(x)) if pd.notnull(x) and isinstance(x, str) else 0)

# 预定义的 MySQL 列最大长度（示例值，可以根据实际情况调整）
mysql_column_max_lengths = {
    'id': 11,
    'name': 100,
    'english_name': 100,
    'gender': 100,
    'birth_place': 100,
    'native_place': 100,
    'job': 100,
    'nationality': 100,
    'description': 65535,
    'education_level': 100,
    'resume': 65535,
    'working_time': 100,
    'institution': 100,
    'account_id': 100,
    'account_name': 100,
    'nick_name': 100,
    'source': 100,
    'url': 1000,
    'followers': 100,
}

# 检查每列的最大长度
try:
    max_lengths = string_lengths.max()
    print("计算最大长度完成.")
except Exception as e:
    print(f"计算最大长度时发生错误: {str(e)}")
    exit()

# 统计超出预定义长度的行数
exceeding_rows = {}

for column, max_length in max_lengths.items():
    if column in mysql_column_max_lengths:
        try:
            if max_length > mysql_column_max_lengths[column]:
                exceeding_rows[column] = df[string_lengths[column] > mysql_column_max_lengths[column]]
        except Exception as e:
            print(f"处理超出长度行数时发生错误: {str(e)}")
            exit()

# 输出超出预定义长度的行数
for column, df_exceeding_rows in exceeding_rows.items():
    try:
        print(f"Number of rows exceeding max length for column '{column}': {len(df_exceeding_rows)}")
        print(df_exceeding_rows)
    except Exception as e:
        print(f"输出超出长度行数时发生错误: {str(e)}")
        exit()

# 处理 CSV 文件中的特殊字符后保存
try:
    df.to_csv(cleaned_csv_file_path, index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)
    print(f"处理 CSV 文件中的特殊字符后保存成功，已保存至 {cleaned_csv_file_path}")
except Exception as e:
    print(f"处理 CSV 文件中的特殊字符时发生错误: {str(e)}")
    exit()
