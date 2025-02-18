import os
import shutil
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 文件路径
original_file_path = 'C:/Users/yuhuo/Documents/Code/pythonProject0611/未关联MCN机构表.xlsx'  # 原始文件路径
output_file_path = os.path.join(os.path.dirname(original_file_path), 'output.xlsx')  # 输出文件路径

# 复制文件，确保不修改原文件
shutil.copyfile(original_file_path, output_file_path)

# 读取复制的Excel文件
df = pd.read_excel(output_file_path)

def fetch_mcn(user_id):
    try:
        # 设置Chrome WebDriver路径
        driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'  # 替换为你的Chrome WebDriver路径
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无界面模式
        driver = webdriver.Chrome(executable_path=driver_path, options=options)

        url = f"https://xd.newrank.cn/tiktok/account?keyWord={user_id}"
        print(f"Fetching URL: {url}")  # 输出正在访问的URL

        # 添加Cookie到请求头
        cookie = 'token=CC7A82B730054DE08EFEEAD2F540399D; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22nr_mi2mm649m%22%2C%22first_id%22%3A%221900b96ff007bb-0d6911a0e77d16-4c657b58-2073600-1900b96ff0114d5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwMGI5NmZmMDA3YmItMGQ2OTExYTBlNzdkMTYtNGM2NTdiNTgtMjA3MzYwMC0xOTAwYjk2ZmYwMTE0ZDUiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJucl9taTJtbTY0OW0ifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22nr_mi2mm649m%22%7D%2C%22%24device_id%22%3A%221900b96ff007bb-0d6911a0e77d16-4c657b58-2073600-1900b96ff0114d5%22%7D; acw_tc=0a47309317181831611717440e003e2d8c5c41e541133e0d51e88e88f18d5a'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Cookie': cookie
        }

        driver.get(url)
        # 等待MCN字段出现
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-tooltip-inner')))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 查找MCN字段
        tooltip_div = soup.find('div', class_='ant-tooltip-inner')
        if tooltip_div:
            print(f"MCN found: {tooltip_div.text.strip()}")  # 输出找到的MCN内容
            return tooltip_div.text.strip()
        print("MCN not found in the response.")
        return None
    except Exception as e:
        print(f"Error fetching data for user_id {user_id}: {e}")
        return None

# 确保目标列存在
if 'mcn_organ_name' not in df.columns:
    df['mcn_organ_name'] = None

# 遍历DataFrame中的每一行
for index, row in df.iterrows():
    url = row['url']
    user_id = row['user_id']
    user_name = row.get('user_name', 'N/A')  # 假设user_name列存在
    mcn_organ_name = row['mcn_organ_name']

    # 仅当 mcn_organ_name 为空时进行查找
    if pd.isna(mcn_organ_name) and pd.notna(url) and isinstance(url, str) and 'douyin' in url:
        mcn_organ_name = fetch_mcn(user_id)
        if mcn_organ_name:
            print(f"user_id: {user_id}, user_name: {user_name}, mcn_organ_name: {mcn_organ_name}")
            df.at[index, 'mcn_organ_name'] = mcn_organ_name
        else:
            print(f"user_id: {user_id}, user_name: {user_name}, Error!")

# 将结果写回到新的Excel文件
df.to_excel(output_file_path, index=False)

print("数据获取完成!")
