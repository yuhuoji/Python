import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_mcn(user_id):
    try:
        # Set up Chrome WebDriver
        driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(executable_path=driver_path, options=options)

        # Open the URL
        url = f"https://xd.newrank.cn/tiktok/account?keyWord={user_id}"
        print(f"Fetching URL: {url}")
        driver.get(url)

        # Find and click the search button
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., '搜索')]")))
        search_button.click()

        # Wait for the response
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-btn-primary')))

        # Extract data from the response
        json_data = driver.execute_script("return document.querySelector('body').innerText")
        mcn_name = json_data.get('data', {}).get('list', [])[0].get('mcn_name')  # Extract MCN name
        if mcn_name:
            print(f"MCN found: {mcn_name}")
            return mcn_name
        else:
            print("MCN not found in the response.")
            return None
    except Exception as e:
        print(f"Error fetching data for user_id {user_id}: {e}")
        return None
    finally:
        driver.quit()

# Search for the given user_id
user_id = '99479153747'
mcn_result = fetch_mcn(user_id)
print(f"MCN for user_id {user_id}: {mcn_result}")
