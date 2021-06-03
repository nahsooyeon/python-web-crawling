import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section3/3-6(all)/chrome/chromedriver.exe')

driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("/Users/devpomme/Desktop/Website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("/Users/devpomme/Desktop/Website2.png")
driver.quit()
