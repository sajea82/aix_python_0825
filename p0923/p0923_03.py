from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# 2. selenium : 자동화 구현
browser = webdriver.Chrome()
url = "https://www.naver.com/"

# 검색부분 - 날씨 입력 > enter : 온도, 날씨를 출력하시오.
browser.get(url)
browser.find_element(By.CLASS_NAME,'')



# # 브라우저 열기
# browser.get(url)
# browser.find_element(By.CLASS_NAME,'MyView-module__link_login___VlF7z').click()
# time.sleep(3)
# elem = browser.find_element(By.ID,'id')
# elem.send_keys('aaa')
# elem2 = browser.find_element(By.ID,'pw')
# elem2.send_keys('1111')
# input() # 꼭 넣어야 화면이 사라지지 않고 그대로 있음

# # selenium 액션 명령어
# ---------
# elem.click() # 클릭
# elem.send_keys(“시가총액”) # 입력창 글자입력
# elem.send_keys(Keys.ENTER) # 키보드 enter키 입력
# browser.switch_to.window(browser.window_handles[1])

# # .env파일 읽기
# load_dotenv()
# print(os.getenv('naver_id'))