from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time




# 구글 트렌드 url
url_ggl_trend = 'https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR'

driver = webdriver.Chrome()
driver.implicitly_wait(5)
time.sleep(5)

driver.get(url_ggl_trend)


# 어제 일별 인기 검색어
# day_trend_xpath = '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/ng-include/div/div/div/div[2]'
#
# day_trend = driver.find_element_by_xpath(day_trend_xpath)
# day_trend_date = day_trend.find_element('div.content-header-title')
#
# print(day_trend_date.text)