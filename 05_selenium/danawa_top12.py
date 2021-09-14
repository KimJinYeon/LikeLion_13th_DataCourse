from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time

# 크롬 창을 띄우지 않고 실행하는 옵션
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("disable-gpu")

# 셀레니움 웹드라이버 실행
driver = webdriver.Chrome('chromedriver', options=chrome_option)
time.sleep(5)
driver.implicitly_wait(5)

# 다나와 url
url_danawa = 'http://www.danawa.com/'

# 웹드라이버 실행
driver.get(url_danawa)
driver.implicitly_wait(5)
time.sleep(5)

# page = driver.page_source
# soup = BeautifulSoup(page, 'html.parser')
# time.sleep(5)
all_product = []
all_price = []

top100 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[7]/div[2]/div[2]/div[2]/div[2]/ul[1]/li[1]')
# //*[@id="top100_0"]/div[2]/div[2]/ul[1]/li[1]
# //*[@id="top100_0"]/div[2]/div[2]/ul[1]/li[2]
print(top100)
#
# time.sleep(5)
# print(top100)
# top100 = top100.select('div.main-top100__right > div.swiper-wrapper')
# time.sleep(5)
# print(top100)
# time.sleep(5)
# for prod_list in top100:
#     p = prod_list.find_all('li')
#     for prod in p:
#         name = prod.find('span', class_='prod-list__txt').text
#         price = prod.find('span', class_='prod-list__price').find('span', class_='num').text
#         all_product.append(name)
#         all_price.append(price)

dict_info = {'제품': all_product, '가격': all_price}

danawa_top100 = pd.DataFrame(dict_info)
danawa_top100.to_csv('danawa_tqp100.csv', index=False, encoding='utf-8-sig')