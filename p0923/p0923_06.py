from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# for i in range(2016,2021):
#     m_url = f"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q={i}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
#     print(m_url)

# # 2. selenium : 자동화 구현
# # 상단 제어창문구 삭제 
#     options = Options()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     browser = webdriver.Chrome(options=options)
#     browser.maximize_window() # 화면 최대창 확대
#     url = m_url
#     browser.get(url)
#     time.sleep(3)   

#     # 파일저장
#     soup = BeautifulSoup(browser.page_source,'lxml')
#     os.makedirs('./p0923/file',exist_ok=True)
#     with open(f'p0923/file/movie_{i}.html','w',encoding='utf-8') as f:
#         f.write(soup.prettify())
#         time.sleep(2)
  
# # 파일저장 (한가지 파일만 저장할때)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0923/file/movie_2016.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())    
#     time.sleep(2)

# 파일변환
# for idx in range(2016,2021):
with open('p0923/file/movie_2016.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
        # print(soup.title)
        # print("파일변환완료")

m_ul = soup.find('ul',{'class':"c-list-basic ty_flow35"})
lis = m_ul.find_all("li")
print("[2016년 영화]")

# 이미지
m_img = lis[0].find('img')['src']
print("이미지 : ",m_img)

# 영화제목
m_tital = lis[0].find("strong",{"class":"tit-g clamp-g"}).get_text(strip=True)
print("영화제목 :",m_tital)

# 누적관객수
m_desc = lis[0].find('p',{'class':'conts-desc clamp-g'}).get_text(strip=True)
print("누적관객수")
print(int(m_desc[3:-2].replace(",","")))

# 개봉날짜
m_date = lis[0].find('span',{'class':'conts-subdesc clamp-g'}).get_text(strip=True)
print("개봉날짜 : ",m_date)
print("-"*60)