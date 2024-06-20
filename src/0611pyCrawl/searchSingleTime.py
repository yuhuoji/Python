import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置ChromeDriver路径（根据您自己的实际路径进行更改）
chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'

# 设置ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置无头模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# 创建ChromeDriver服务
service = Service(chromedriver_path)


def fetch_mcn_with_login_cookies(user_id, cookies):
    url = f"https://xd.newrank.cn/tiktok/account?keyWord={user_id}"
    print(f"Fetching URL: {url}")

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 打开页面
        driver.get(url)

        # 设置cookie
        for cookie in cookies:
            driver.add_cookie(cookie)

        # 再次打开页面以确保cookie生效
        driver.get(url)

        # 增加等待时间，确保页面完全加载
        time.sleep(5)

        # 打印页面源代码以进行调试
        print(driver.page_source)

        # 尝试找到MCN的元素
        try:
            tooltip_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "ant-tooltip-inner")]'))
            )
            mcn_organ_name = tooltip_element.text
        except Exception as e:
            print(f"MCN not found in the response: {e}")
            mcn_organ_name = None

        driver.quit()

        if mcn_organ_name:
            return mcn_organ_name
        else:
            return "Error!"
    except Exception as e:
        print(f"Error fetching data for user_id {user_id}: {e}")
        return "Error!"


# 示例：获取一个user_id的MCN，同时设置cookie
user_id = "70956164696"
cookies = [
    {'name': 'sensorsdata2015jssdkcross',
     'value': '%7B%22distinct_id%22%3A%22nr_mi2mm649m%22%2C%22first_id%22%3A%221900b96ff007bb-0d6911a0e77d16-4c657b58-2073600-1900b96ff0114d5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwMGI5NmZmMDA3YmItMGQ2OTExYTBlNzdkMTYtNGM2NTdiNTgtMjA3MzYwMC0xOTAwYjk2ZmYwMTE0ZDUiLCIkaWRlbnRpdHlfbG9naW5faWQiOiJucl9taTJtbTY0OW0ifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22nr_mi2mm649m%22%7D%2C%22%24device_id%22%3A%221900b96ff007bb-0d6911a0e77d16-4c657b58-2073600-1900b96ff0114d5%22%7D'},
    {'name': 'token', 'value': 'FA7B72AB17B64E2B88ED9D00023DFD19'},
    {'name': 'acw_tc', 'value': '0a472f8c17183350746201979e005dad870c45e7f04120a9c6866a8da0f12c'}
]

mcn_organ_name = fetch_mcn_with_login_cookies(user_id, cookies)
print(f"user_id: {user_id}, mcn_organ_name: {mcn_organ_name}")
