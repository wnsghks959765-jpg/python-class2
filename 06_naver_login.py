import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

naver_login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
driver.get(naver_login_url)
time.sleep(1)

id_input = driver.find_element(By.CSS_SELECTOR, 'input#id')
id_input.send_keys('your_id')

password_input = driver.find_element(By.CSS_SELECTOR, 'input#pw')
password_input.send_keys('your_password')

# 로그인 버튼은 창 너비에 따라 두 개 중 하나만 보여서, 비밀번호 칸에서 엔터를 친다
password_input.send_keys(Keys.ENTER)
