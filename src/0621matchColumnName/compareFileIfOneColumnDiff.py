import requests
import openpyxl
import pandas as pd
import os


def read_prefix_from_xls(filename):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append({'账号': row[0], 'uid': None})
    return data


def fetch_data(page):
    url = f"https://dyapi.huitun.com/user/mcnUser?_t=1719887059788&mcnId=599&from={page}"
    response = requests.get(url)
    return response.json()


def extract_uids(json_data):
    uids = []
    if 'data' in json_data:
        for item in json_data['data']:
            uids.append({'账号': item['nickName'], 'uid': item['uid']})
    return uids


def update_excel_with_uids(data, uids, original_filename):
    # Create a DataFrame from the Excel data
    df = pd.DataFrame(data)

    # Create a DataFrame from the fetched uids
    uids_df = pd.DataFrame(uids)

    # Merge the two DataFrames on the '账号' column
    merged_df = pd.merge(df, uids_df, on='账号', how='left')

    # Fill the uid column in the original DataFrame
    df['uid'] = merged_df['uid_y']

    # Save the updated DataFrame back to Excel
    base_name = os.path.basename(original_filename)
    output_filename = f"updated_{base_name}"
    output_path = os.path.join(os.path.dirname(original_filename), output_filename)
    df.to_excel(output_path, index=False)
    print(f"数据已保存到 {output_path}")


def main():
    prefix_filename = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0702HTTPRequest/乾派文化.xlsx"

    data = read_prefix_from_xls(prefix_filename)

    all_uids = []
    page = 1

    while True:
        json_data = fetch_data(page)
        if 'data' not in json_data or not json_data['data']:
            break
        uids = extract_uids(json_data)
        all_uids.extend(uids)
        page += 1

    update_excel_with_uids(data, all_uids, prefix_filename)


if __name__ == "__main__":
    main()
