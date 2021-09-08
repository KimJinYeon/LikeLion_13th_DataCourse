from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 01 우리가 가져올 URL
# 02 내가 원하는 정보의 위치(span, id)

url = 'https://finance.naver.com/sise'
page = urlopen(url)

# 구체적인 html 정보 확인하고, 구조화
soup = BeautifulSoup(page, 'html.parser')
KOSPI = soup.find('span', id='KOSPI_now')
KOSDAQ = soup.find('span', id='KOSDAQ_now')
KPI200 = soup.find('span', id='KPI200_now')
popularList = soup.find('ul', id='popularItemList')
popularList = popularList.find_all('a')
print('현재 코스피는: ', KOSPI.text)
print('현재 코스닥은: ', KOSDAQ.text)
print('현재 코스피200은: ', KPI200.text)
print(popularList.text)