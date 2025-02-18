import json
import pandas as pd
import openpyxl
import os

def read_txt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def parse_json_objects(content):
    json_objects = []
    for json_str in content.split('\n\n'):
        if json_str.strip():
            json_objects.append(json.loads(json_str.strip()))
    return json_objects

def extract_uids(json_objects):
    uids_dict = {}
    for obj in json_objects:
        for item in obj['data']:
            uids_dict[item['nickName']] = item['uid']
    return [{'nickName': k, 'uid': v} for k, v in uids_dict.items()]

def read_excel_file(filepath):
    return pd.read_excel(filepath)

def update_excel_with_uids(excel_df, uids):
    uids_df = pd.DataFrame(uids)
    merged_df = pd.merge(excel_df, uids_df, left_on='标题', right_on='nickName', how='left')
    excel_df['uid'] = merged_df['uid']
    return excel_df

def save_to_excel(df, original_filepath):
    base_name = os.path.basename(original_filepath)
    output_filename = f"updated_uid_{base_name}"
    output_path = os.path.join(os.path.dirname(original_filepath), output_filename)
    df.to_excel(output_path, index=False)
    print(f"数据已保存到 {output_path}")

def main():
    txt_filepath = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0702HTTPRequest/response.txt"
    excel_filepath = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0702HTTPRequest/圆宵文化.xlsx"

    # 读取和解析txt文件
    txt_content = read_txt_file(txt_filepath)
    json_objects = parse_json_objects(txt_content)

    # 提取UIDs
    uids = extract_uids(json_objects)

    # 读取Excel文件
    excel_df = read_excel_file(excel_filepath)

    # 更新Excel文件
    updated_df = update_excel_with_uids(excel_df, uids)

    # 保存更新后的Excel文件
    save_to_excel(updated_df, excel_filepath)

if __name__ == "__main__":
    main()