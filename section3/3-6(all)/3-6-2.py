import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# CLI 환경 세팅

# chrome_options = Options()
# chrome_options.add_argument("--headless") # 브라우저 없음(CLI모드)
# chrome_options.add_argument('--log-level=3')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section3/3-6(all)/chrome/chromedriver')
driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get('https://google.com')

# driver.save_screenshot("/Users/devpomme/Desktop/Website1_ch.png")
#
# driver.get('https://www.daum.net')
#
# driver.save_screenshot("/Users/devpomme/Desktop/Website2_ch.png")

driver.quit()
