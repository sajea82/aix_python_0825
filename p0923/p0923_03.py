from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# .env파일읽기
load_dotenv()
print(os.getenv('naver_id'))
