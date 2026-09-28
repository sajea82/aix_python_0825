from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv



# # 2-2. selenium : 자동화 도구 - 스크롤 사용
# url = "https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)
# time.sleep(2)
# # 스크롤 추가
# # execute_script : 자바스크립트 언어 사용가능
# # 현재 스크롤 높이 가져옴
# prev_height = browser.execute_script("return document.body.scrollHeight")

# while True:
#     # 스크롤 높이 출력
#     print('높이 : ',prev_height)
#     # 스크롤 내리기
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(2)
#     # 스크롤이 추가 되었는지 확인
#     next_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == next_height:
#         break
#     prev_height = next_height


# 3. 파일 BeautifulSoup변환
with open('p0928/file/flight2.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

flights = soup.find_all('div',{'class':'domestic_Flight__8bR_b'})
print(len(flights))

# 항공사,출발시간,도착시간,가격-문자열,가격-숫자형
for flight in flights:

    airline = flight.find('b',{'class':'airline_name__0Tw5w'}).get_text(strip=True)

    routes = flight.find_all('b',{'class':'route_time__xWu7a'})
    route1 = routes[0].get_text(strip=True)
    route2 = routes[1].get_text(strip=True)

    price = flight.find('i',{'class':'domestic_num__ShOub'}).get_text(strip=True)
    i_price = int(price.replace(',',''))

    if i_price < 70000 :
        print(airline,route1,route2,price,i_price)




# 70000원 이하에 있는 비행기를 출력

# 3. 파일 BeautifulSoup변환
# with open('C:/workspace/python/p0928/file/flight2.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')

# items = soup.find_all('li',{'class':'gc-thumbnail-type-seller-card-wrapper css-13wylk3'})
# count=0
# v = items[0].find('span',{'class':'css-1llao6q'})

# print(v)
# for cost in range(len(items)):
#     f_cost = items[cost].find('span',{'class':'css-1llao6q'}).get_text(strip=True)
#     get_cost = int(f_cost.replace(',',''))
#     if get_cost<=70000: count=count+1

# print(len(items))
# print(len(items),f_cost)
# print("70,000원 이하의 숙박시설 갯수는 : ",count)

# y_datas = items.find_all('div',{'data-known-size':'228'})
# print(len(y_datas))

# # 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/flight2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# print('완료')

# 1.자바스크립트가 포함되어 있으면 - selenium 사용
# 2. find,find_all
# 3. [속성]
# --------------
# 웹 변수 -> 타입:str
# int,float 계산가능

# 문자에 ,단위 표기가 포함되어 있으면
# replace(',','')

# a = '1000원'
# int(a[:-1])