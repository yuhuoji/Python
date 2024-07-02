import requests
import xlrd
import openpyxl


def fetch_data(page):
    url = f"https://dyapi.huitun.com/user/mcnUser?_t=1719887059788&mcnId=599&from={page}"
    response = requests.get(url)
    response.raise_for_status()  # 检查是否成功响应
    return response.json()


def extract_uids(json_data):
    uids = []
    for user in json_data.get('data', []):
        uids.append(user['uid'])
    return uids


def read_prefix_from_xls(filename):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)  # 读取第一个工作表
    prefixes = []
    for row_idx in range(1, sheet.nrows):  # 从第二行开始，假设第一行是表头
        prefixes.append(sheet.cell(row_idx, 0).value)
    return prefixes


def save_to_excel_with_prefix(uids, prefix):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "UIDs"

    ws.append(["UID"])  # 添加表头
    for uid in uids:
        ws.append([uid])

    output_filename = f"{prefix}_uids.xlsx"
    wb.save(output_filename)
    return output_filename


def main():
    prefix_filename = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0702HTTPRequest/乾派文化.xlsx"
    prefixes = read_prefix_from_xls(prefix_filename)

    all_uids = []
    page = 1

    while True:
        json_data = fetch_data(page)
        if not json_data['data']:
            break
        uids = extract_uids(json_data)
        all_uids.extend(uids)
        page += 1

    for prefix in prefixes:
        save_to_excel_with_prefix(all_uids, prefix)
        print(f"数据已保存到 {prefix}_uids.xlsx 文件中")


if __name__ == "__main__":
    main()
